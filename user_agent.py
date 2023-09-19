import random

user_agents = [
    # Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    # Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    # Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15",
    # Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    # Opera
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    # Internet Explorer
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    # Mobile user-agents
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]


ip_addresses = [
    "72.44.114.170",
    "21.58.210.140",
    "176.63.172.48",
    "216.69.70.144",
    "149.222.57.23",
    "85.241.212.224",
    "137.2.7.166",
    "227.5.126.201",
    "215.248.205.18",
    "83.108.151.5",
    "126.27.160.186",
    "214.136.128.39",
    "12.27.6.39",
    "71.243.133.226",
    "98.149.67.49",
    "72.145.157.20",
    "189.169.122.56",
    "111.100.81.206",
    "195.164.125.192",
    "83.146.47.14",
    "174.107.156.29",
    "75.237.162.235",
    "6.180.118.180",
    "32.229.183.140",
    "71.195.8.88",
    "122.176.166.225",
    "143.165.118.110",
    "76.241.66.141",
    "91.183.43.174",
    "166.176.35.116",
    "235.146.230.61",
    "102.4.175.119",
    "162.127.2.255",
    "81.186.68.144",
    "72.238.73.31",
    "22.214.121.228",
    "198.165.164.57",
    "91.120.117.197",
    "134.226.116.7",
    "232.54.214.211",
    "84.252.106.67",
    "221.13.209.12",
    "247.78.189.54",
    "159.64.199.35",
    "21.39.165.46",
    "126.63.110.215",
    "201.81.139.170",
    "80.17.237.248",
    "18.219.108.151",
    "60.145.26.79",
    "233.97.19.254",
    "169.21.203.163",
    "57.168.170.97",
    "5.24.62.155",
    "242.41.252.215",
    "9.25.139.195",
    "187.23.10.64",
    "110.103.6.54",
    "76.127.226.189",
    "11.92.83.56",
    "77.140.224.93",
    "140.59.79.45",
    "232.177.203.40",
    "64.105.201.180",
    "219.206.205.245",
    "40.118.20.188",
    "82.118.181.246",
    "199.159.166.105",
    "57.76.203.200",
    "168.137.72.58",
    "209.250.64.144",
    "241.216.13.197",
    "3.4.98.40",
    "30.234.193.239",
    "199.171.197.152",
    "226.149.190.104",
    "124.250.235.195",
    "249.62.247.44",
    "39.45.28.35",
    "242.245.228.228",
    "109.102.23.111",
    "180.246.252.86",
    "166.12.67.199",
    "189.64.49.202",
    "240.244.12.174",
    "63.147.5.252",
    "211.112.45.219",
    "238.161.118.111",
    "38.42.22.156",
    "77.36.99.77",
    "184.200.3.193",
    "168.101.116.186",
    "137.121.165.242",
    "6.137.234.201",
    "152.113.170.89",
    "17.171.223.161",
    "18.25.191.13",
    "171.105.63.20",
    "95.216.66.58",
    "192.93.0.171",
    "137.146.19.51",
    "235.152.62.102",
    "143.246.210.255",
    "146.90.254.145",
    "39.212.152.107",
    "117.255.202.228",
    "238.91.247.159",
    "30.241.100.69",
    "72.123.247.27",
    "161.65.92.120",
    "188.193.149.163",
    "14.168.196.100",
    "118.186.136.185",
    "24.239.141.253",
    "47.36.233.97",
    "95.137.3.44",
    "196.39.125.100",
    "9.111.41.242",
    "195.185.30.25",
    "137.105.226.203",
    "209.179.84.51",
    "250.229.9.236",
    "185.180.61.70",
    "188.10.4.38",
    "163.68.87.51",
    "53.103.36.115",
    "100.68.44.180",
    "108.147.201.56",
    "201.166.2.196",
    "146.195.93.225",
    "57.30.17.27",
    "21.255.194.130",
    "44.246.239.215",
    "98.16.47.194",
    "8.202.61.155",
    "173.73.241.128",
    "174.200.41.189",
    "102.84.119.160",
    "31.103.51.198",
    "3.81.148.92",
    "20.196.62.240",
    "82.235.183.85",
    "5.129.167.215",
    "90.95.240.71",
    "108.237.42.239",
    "218.131.170.220",
    "186.186.29.3",
    "149.204.207.5",
    "47.43.11.0",
    "238.36.117.84",
    "246.39.197.243",
]

proxies = [
    "186.121.235.222:8080",
    "118.69.111.51:8080",
    "37.187.25.85:80",
    "66.70.176.151:8080",
    "34.23.45.223:80",
    "161.97.93.15:80",
    "47.74.152.29:8888",
    "43.156.77.127:80",
    "45.8.145.72:80",
    "143.198.228.250:80",
    "190.128.241.102:80",
    "197.255.126.69:80",
    "45.63.25.2:8888",
    "62.113.228.225:80",
    "187.217.54.84:80",
    "34.75.202.63:80",
    "98.126.214.163:80",
    "197.243.20.178:80",
    "146.59.199.12:80",
]


def get_user_agent():
    return random.choice(user_agents)


def get_ip_address():
    return random.choice(ip_addresses)


def get_proxies():
    proxy = random.choice(proxies)
    return {
        "http": "http://" + proxy,
    }


def get_headers():
    return {"User-Agent": get_user_agent(), "Forwarded": get_ip_address()}
