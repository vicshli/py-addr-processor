import math

def get_addr_tag(addr, tag_len):
    return addr[:tag_len]

def get_addr_index(addr, index_len, tag_len):
    end_index = tag_len + index_len
    return addr[tag_len : end_index]

def get_addr_offset(addr, offset_len):
    addr_len = len(addr)
    start_index = addr_len - offset_len
    # return the last `offset_len` bits of addr
    return addr[start_index:]

def get_offset_len(block_size):
    return (int)(math.log(block_size, 2))

def get_index_len(block_num, set_size):
    num_of_sets = block_num / set_size
    return (int) (math.log(num_of_sets, 2))

def get_tag_len(addr_len, index_len, offset_len):
    return (int) (addr_len - index_len - offset_len)

def is_divisible(numerator, denominator):
    return numerator % denominator == 0

def hex_to_bin(hex_str):
    dec_int = int(hex_str, 16)
    bin_int = bin(dec_int)
    bin_str = str(bin_int)[2:]  # strip out 0b prefix
    return bin_str

def bin_to_hex(bin_str):
    dec_int = int(bin_str, 2)
    hex_int = hex(dec_int)
    hex_str = str(hex_int)[2:]  # strip out 0x prefix
    hex_str = hex_str.upper()
    return hex_str

def partition_addr(addr, tag_len, index_len, offset_len):
    addr_tag = get_addr_tag(addr, tag_len)
    addr_index = get_addr_index(addr, index_len, tag_len)
    addr_offset = get_addr_offset(addr, offset_len)
    return addr_tag, addr_index, addr_offset

def batch_bin_to_hex(addr1, addr2, addr3):
    return bin_to_hex(addr1), bin_to_hex(addr2), bin_to_hex(addr3)

def main():
    # address_hex = "0xABCDEF"
    address_hex = input("Address in hex:")
    block_num = int(input("Number of blocks in cache:"))
    set_size = int(input("Size of each set (how many ways associative?): "))
    block_size = int(input("Block size (size of each block in cache):"))

    address_bin = hex_to_bin(address_hex)

    print("The address you entered is {} (binary {})\
        ".format(address_hex, address_bin))

    print("Number of blocks: {}\t Size of each set: {}\t Size of each block: {}\
        ".format(block_num, set_size, block_size))

    address_len = len(address_bin)
    index_len = get_index_len(block_num, set_size)
    offset_len = get_offset_len(block_size)
    tag_len = get_tag_len(address_len, index_len, offset_len)

    address_tag, address_index, address_offset = partition_addr(\
        address_bin, tag_len, index_len, offset_len)

    address_tag_hex, address_index_hex, address_offset_hex = batch_bin_to_hex(\
        address_tag, address_index, address_offset)

    print('Tag (bin) is\t\t{}\nIndex (bin) is\t\t{}\nOffset (bin) is\t\t{}\
        '.format(address_tag, address_index, address_offset))

    print('Tag (hex) is\t\t{}\nIndex (hex) is\t\t{}\nOffset (hex) is\t\t{}\
        '.format(address_tag_hex, address_index_hex, address_offset_hex))


if __name__ == '__main__':
    main()
