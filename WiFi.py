from subprocess import check_output


profile_name_raw = ''
profile_names = ''
key_dictionary = {}
l1 = []
x = check_output('netsh wlan show profiles', shell=True)
for i in x:
    profile_name_raw = profile_name_raw + chr(i)

for j in range(len(profile_name_raw)):
    temp = profile_name_raw[j]
    if profile_name_raw[j] == ':':
        if profile_name_raw[j + 1] == " ":
            for k in range(2, 64):
                if profile_name_raw[j + k] == '\r':
                    profile_names = profile_names + "@"
                    break
                else:
                    profile_names = profile_names + profile_name_raw[j + k]

        else:
            continue
    else:
        continue
profile_names = profile_names.rstrip("@")
l1 = profile_names.split(sep="@")
for k in l1:
    key_string_raw = check_output('netsh wlan show profile ' + "name=" + f'"' + str(k) + f'"' + ' key=clear', shell=True, universal_newlines=True)
    key_string_raw = str(key_string_raw)
    index = key_string_raw.find('Key Content')
    if index == -1:
        continue
    else:
        l = 0
        while True:
            key_string = " "
            l = l + 1
            if key_string_raw[index + l] == ':':
                semi_index = index + l
                break
        for m in range(2, 64):
            if key_string_raw[semi_index + m] == '\n':
                key_string = key_string + " "
                break
            else:
                key_string = key_string + key_string_raw[semi_index + m]
                key_dictionary[k] = key_string
print(key_dictionary)
