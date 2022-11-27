import re
import urllib.request
import os


def get_host_infos(url):
    response = urllib.request.urlopen(url).read().decode('utf-8')

    ipv4_block_pattern = re.compile(
        '<td><ul class="comma-separated">(.+?)</ul>')
    ipv4_block = re.findall(ipv4_block_pattern, response)[0]

    ipv4_pattern = re.compile('<li>(.+?)</li>')
    ipv4 = list()
    for each in re.findall(ipv4_pattern, ipv4_block):
        ipv4.append(each)

    return ipv4


def write_to_host(name_to_ipv4):
    init_host_path = os.path.join(os.path.dirname(__file__),
                                  'initialized_hosts')
    init_content = ''
    with open(init_host_path, 'r', encoding='utf8') as fr:
        init_content = fr.read()

    with open('C:\Windows\System32\drivers\etc\hosts', 'w',
              encoding='UTF-8') as fw:
        fw.write(init_content)
        for each in name_to_ipv4:
            domain_name = each[0]
            ipv4s = each[1]
            for ipv4 in ipv4s:
                fw.write(ipv4 + '    ' + domain_name + '\n')


def update_hosts():
    domain_names = ['github.global.ssl.fastly.net', 'github.com']

    domain_name_to_ipv4 = list()
    for each in domain_names:
        url = 'https://www.ipaddress.com/site/' + each
        ipv4s = get_host_infos(url)

        domain_name_to_ipv4.append((each, ipv4s))
    write_to_host(domain_name_to_ipv4)


def update_google_translate():
    # cdn_hosts = ' https://cdn.jsdelivr.net/gh/googlehosts/hosts@master/hosts-files/hosts '
    # google_hosts = urllib.request.urlopen(cdn_hosts).read().decode('utf8')

    # with open('C:\Windows\System32\drivers\etc\hosts', 'w', encoding='UTF-8') as fw:
        # fw.write(google_hosts) 
    pass


def restore_hosts():
    init_host_path = os.path.join(os.path.dirname(__file__), 'initialized_hosts')
    init_content = ''
    with open(init_host_path, 'r', encoding='utf8') as fr:
        init_content = fr.read()

    with open('C:\Windows\System32\drivers\etc\hosts', 'w', encoding='UTF-8') as fw:
        fw.write(init_content)


def main():
    print('Function list:\n 1. update github;\n 2. update google;\n 3. restore hosts;\n Please input your choice (any other input to exit):\n')

    choice = int(input())

    if choice == 1:
        update_hosts()
        print('The github hosts have been injected into hosts.')
    elif choice == 2:
        update_google()
        print('The Google hosts have been injected into hosts.')
    elif choice == 3:
        restore_hosts()
        print('The hosts has been restored.')
    else:
        print('Do not match any actions.')


if __name__ == '__main__':
    main()