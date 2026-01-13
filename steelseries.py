#!/usr/bin/env python3

import argparse
import struct
import usb.core

DEFAULT_COLOUR = "1F0700"
DEFAULT_VENDOR = "1038"
DEFAULT_PRODUCT = "183c"


def colour_packet(
    rgb0: str,
    rgb1: str,
    rgb2: str,
    rgb3: str,
    rgb4: str,
    rgb5: str,
    rgb6: str,
    rgb7: str,
    rgb8: str,
    rgb9: str,
):
    result = bytearray()
    result.append(0x21)
    result.append(0xFF)
    result.append(0x03)
    result.extend(bytes.fromhex(rgb0))
    result.extend(bytes.fromhex(rgb1))
    result.extend(bytes.fromhex(rgb2))
    result.extend(bytes.fromhex(rgb3))
    result.extend(bytes.fromhex(rgb4))
    result.extend(bytes.fromhex(rgb5))
    result.extend(bytes.fromhex(rgb6))
    result.extend(bytes.fromhex(rgb7))
    result.extend(bytes.fromhex(rgb8))
    result.extend(bytes.fromhex(rgb9))
    return bytes(result)


def set_colour(vendor_id: int, product_id: int, colour: str):
    # find horrible SteelSeries Rival 5
    dev = usb.core.find(idVendor=0x1038, idProduct=0x183C)
    cfg = dev.get_active_configuration()
    report_if = cfg.interfaces()[0]

    if dev.is_kernel_driver_active(0):
        dev.detach_kernel_driver(0)
    dev.ctrl_transfer(
        0x21,  # REQUEST_TYPE_CLASS | RECIPIENT_INTERFACE | ENDPOINT_OUT
        0x09,  # SET_REPORT
        0x200,  # reportID 0, reportType (output) 2
        0,  # USB interface 0
        colour_packet(
            colour,
            colour,
            colour,
            colour,
            colour,
            colour,
            colour,
            colour,
            colour,
            colour,
        ),
    )


def main():
    parser = argparse.ArgumentParser(
        description="Set a fixed colour for a SteelSeries Rival mouse"
    )
    parser.add_argument(
        "--vendor-id", type=str, default=DEFAULT_VENDOR, help="USB vendor ID"
    )
    parser.add_argument(
        "--device-id", type=str, default=DEFAULT_VENDOR, help="USB device ID"
    )
    parser.add_argument(
        "--colour", type=str, default=DEFAULT_COLOUR, help="Hexadecimal RGB value"
    )
    args = parser.parse_args()
    set_colour(int(args.vendor_id, 16), int(args.device_id, 16), args.colour)


if __name__ == "__main__":
    main()
