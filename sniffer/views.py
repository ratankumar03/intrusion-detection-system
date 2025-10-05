from django.shortcuts import render
# sniffer/views.py
from django.shortcuts import render
from django.http import HttpResponse
from scapy.all import *
from .models import CapturedPacket
import csv

# def test(request):
#     return HttpResponse('testing the page')
def index(request):
    return render(request,'index.html')

def capture_packets(request):
    packets = sniff(count=100)  # Capture 10 packets (modify as needed)

    # Save captured packets to database
    for packet in packets:
        if packet.haslayer(IP):
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            ip_proto = packet[IP].proto
            length = len(packet)
            payload = str(packet.payload)

            CapturedPacket.objects.create(
                source_ip=ip_src,
                destination_ip=ip_dst,
                protocol=ip_proto,
                length=length,
                payload=payload
            )

    # Generate CSV file
    csv_data = [['Source IP', 'Destination IP', 'Protocol', 'Length', 'Payload']]
    packets = CapturedPacket.objects.all()
    for packet in packets:
        csv_data.append([packet.source_ip, packet.destination_ip, packet.protocol, packet.length, packet.payload])

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="captured_packets.csv"'
    csv_writer = csv.writer(response)
    csv_writer.writerows(csv_data)

    return response


# Create your views here.

def home(request):
    return render(request,'home.html')
def show1(request):
    return render(request,'show.html')

def show(request):
    u=CapturedPacket.objects.all()
    return render(request,'show.html',{'u':u})
