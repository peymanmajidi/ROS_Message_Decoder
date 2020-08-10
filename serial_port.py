import serial.tools.list_ports

def list(print_on_screen=False):
    print('Search...\r', end='')
    ports = serial.tools.list_ports.comports(include_links=False)
    print('                       \r', end='')
    results = []
    for port in ports:
        if print_on_screen:
            print('|'+ port.device)
        results.append(port.device)
    return results
