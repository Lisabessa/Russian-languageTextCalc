import processing_funcs_module

request = input()
while request != "ВЫХОД":
    if processing_funcs_module.calc(request) != -1:
        print(processing_funcs_module.calc(request))
    print()
    print()
    request = input()