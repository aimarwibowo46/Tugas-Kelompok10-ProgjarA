
import argparse, random, socket, zen_utils
import sys, random, multiprocessing

HOST = "127.0.0.1"
PORT = 1060
NUMJOBS = 10

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

def worker(address, i, data):
    # membuat socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect socket
    sock.connect(address)

    message = ""
    for ii in data: # untuk setiap ii dalam data
        
        #proses kirim ke server
        ii = ii.strip() # dilakukan strip terlebih dahulu, karena di paling kanan masih ada newline
        len_msg = b"%03d" % (len(ii),) # panjang pesan
        msg = len_msg + bytes(ii, encoding="ascii")
        sock.sendall(msg) # mengirim pesan

        #menerima hasil kerja server
        len_msg = recvall(sock, 3) # menerima panjang pesan
        message = recvall(sock, int(len_msg)) # menerima pesan yang masuk
        message = str(message, encoding="ascii")
    print('klien ', i, '-> ',message)
    sock.close()

if __name__ == '__main__':
    # membaca input.txt. dan disimpan menjadi list dalam data
    f = open("input.txt")
    data = f.readlines()
    f.close()

    address = (HOST, PORT)
    jobs = [] # akan berisi list of jobs

    # proses inisiasi jobs
    for i in range(NUMJOBS):
        # untuk menjalankan banyak proses
        # targetnya ada fungsi worker, dengan arguments yg berisi address dari host & port, nomor numjobs,
        # dan salinan dari data
        p = multiprocessing.Process(target=worker, args=(address, i, data))

        # hasil p akan di append ke dalam list jobs
        jobs.append(p)
    print("JOBS:", len(jobs))

    # mulai start proses jobsnya
    for p in jobs:
        p.start()

    # setelah proses selesai, dilakukan join. thread utama akan menunggu sampai semua join.
    for p in jobs:
        p.join()

# vim:sw=4:ai
