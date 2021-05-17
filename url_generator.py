import requests
import ssdeep
import string
import json


def extract_name(url):
    domain = url.replace("https://www.", "")
    domain = domain.replace("http://www.", "")
    domain = domain.replace("www.", "")
    domain = domain.split(".", 1)[0]
    arr = url.split(domain, 1)
    dict = {
        "scheme": arr[0],
        "subdomain": domain,
        "top_level_domain": arr[1]
    }
    return dict


def addition(url):
    url_dict = extract_name(url)
    scheme = url_dict["scheme"]
    top_level_domain = url_dict["top_level_domain"]
    url = url_dict["subdomain"]
    try:
        file_ptr = open("url_to_check.json", 'w')
        print("[", file=file_ptr)
        for i in string.ascii_lowercase:
            dict = {
                "url": f"{scheme + url+i + top_level_domain}",
                "method": "addition"
            }
            dict_json = json.dumps(dict, indent=4)
            # if i != 'z':
            print(dict_json+',', file=file_ptr)
            # else:
            # print(dict_json, file=file_ptr)
        # print("]", file=file_ptr)
    finally:
        file_ptr.close()


def mapping():
    dict = {}
    dict["a"] = "sz"
    dict["b"] = "vn"
    dict["c"] = "xv"
    dict["d"] = "sf"
    dict["e"] = "wr"
    dict["f"] = "dg"
    dict["i"] = "uo"
    dict["g"] = "fh"
    dict["k"] = "jl"
    dict["l"] = "km"
    dict["m"] = "nk"
    dict["n"] = "bm"
    dict["o"] = "ip"
    dict["p"] = "ol"
    dict["q"] = "wa"
    dict["r"] = "et"
    dict["s"] = "ad"
    dict["t"] = "ry"
    dict["u"] = "yi"
    dict["v"] = "cb"
    dict["w"] = "qe"
    dict["x"] = "zc"
    dict["y"] = "tu"
    dict["z"] = "ax"
    return dict


def substitution(url, pos):
    list = []
    url_dict = extract_name(url)
    scheme = url_dict["scheme"]
    top_level_domain = url_dict["top_level_domain"]
    url = url_dict["subdomain"]
    if pos >= len(url)-1:
        return list

    dict = mapping()
    for i in range(pos, len(url)):
        new_url1 = url[:pos] + dict[url[pos]][0] + url[pos+1:]
        list.append(new_url1)
        new_url2 = url[:pos] + dict[url[pos]][1] + url[pos+1:]
        list.append(new_url2)
        # list += substitution(url, pos+1)
    try:
        file_ptr = open("url_to_check.json", 'a')
        for i in list:
            dict = {
                "url": f"{scheme + i + top_level_domain}",
                "method": "substitution"
            }
            dict_json = json.dumps(dict, indent=4)
            print(dict_json+',', file=file_ptr)
    finally:
        file_ptr.close()

    return list


def omission(url):
    url_dict = extract_name(url)
    scheme = url_dict["scheme"]
    top_level_domain = url_dict["top_level_domain"]
    url = url_dict["subdomain"]
    try:
        file_ptr = open("url_to_check.json", 'a')
        for i in range(len(url)):
            s = url[:i] + url[i+1:]
            dict = {
                "url": f"{scheme + s + top_level_domain}",
                "method": "omission"
            }
            dict_json = json.dumps(dict, indent=4)
            print(dict_json+',', file=file_ptr)
    finally:
        file_ptr.close()


def sub_domain(url):
    url_dict = extract_name(url)
    scheme = url_dict["scheme"]
    top_level_domain = url_dict["top_level_domain"]
    url = url_dict["subdomain"]
    try:
        file_ptr = open("url_to_check.json", 'a')
        for i in range(len(url)):
            s = url[:i+1] + "." + url[i+1:]
            dict = {
                "url": f"{scheme + s + top_level_domain}",
                "method": "subdomain"
            }
            dict_json = json.dumps(dict, indent=4)
            if i != len(url)-1:
                print(dict_json+',', file=file_ptr)
            else:
                print(dict_json, file=file_ptr)
        print("]", file=file_ptr)
    finally:
        file_ptr.close()


def running():
    try:
        score = []
        # f = open("url_to_check.json", "r")
        with open("url_to_check.json") as f:
            data = json.load(f)
        for i in data:
            details_dict = i
            try:
                r = requests.get(details_dict["url"])
                if r.status_code == 200:
                    details_dict["status"] = "available"
                else:
                    details_dict["status"] = "not-available"
                hash_value = ssdeep.hash(r.text)
                details_dict["hash"] = hash_value
                score.append(details_dict)
            except requests.exceptions.RequestException as e:
                # raise SystemExit(e)
                print("line91")
        # print("line92")
        # print(score)
        try:
            file_ptr = open("phishing_domains.json", 'w')
            print(json.dumps(score, indent=4), file=file_ptr)
        finally:
            file_ptr.close()
    finally:
        f.close()
    return


def computing_similarity(url):
    try:
        r = requests.get(url)
        score = []
        hash1 = ssdeep.hash(r.text)
        with open("phishing_domains.json") as f:
            data = json.load(f)
        for i in data:
            details_dict = i
            val = ssdeep.compare(i["hash"], hash1)
            i["compare"] = val
            score.append(i)
        print(score)
    except requests.exceptions.RequestException as e:
        print("Please enter valid URL to compare")
        print(url, " does not exist")


addition("https://www.google.com")
omission("https://www.google.com")
substitution("www.google.com", 0)
sub_domain("https://www.google.com")

# running()
# computing_similarity("https://www.google.com")
