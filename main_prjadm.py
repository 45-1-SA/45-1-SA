from modules.xdb_ram import XmlParser  # ������ ����������� xdb->ram
from modules.ram_dbd import RamDbd  # ������ ����������� ram->db
from modules.dbd_ram import DbdRam  # ������ ����������� db->ram
from modules.ram_xdb import XmlMaker  # ������ ����������� ram->xdb
import argparse  # ��������� ����������� ���������� ��������� ���������� �������
import os.path  # ��������� ������ ��� ������ � ������

if __name__ == "__main__":
    #
    # �������������� XDB -> RAM -> DBD
    #
    parser = argparse.ArgumentParser(description='��������� �������������� ������.')

    parser.add_argument('-f', '--file', default='materials/prjadm.xdb',
                        help='�������������� XDB -> RAM -> DBD.')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print("����� {0} �� ����������.".format(args.file))
        exit(-1)

    ram = XmlParser(args.file).make_ram()

    dbd_create = RamDbd(args.file.replace('.xdb', '.db'), ram)

    print("����������� XDB -> RAM -> DBD �������.\n ����� ���� - prjadm.db")
    #
    # �������������� DBD -> RAM - > XDB2
    #
    parser2 = argparse.ArgumentParser(description='��������� �������������� ������.')

    parser2.add_argument('-f', '--file', default='materials/prjadm.db',
                        help='�������������� DBD -> RAM - > XDB2.')

    args = parser2.parse_args()

    ram = DbdRam(args.file).schema

    xml2 = XmlMaker(ram).make_xdb()

    # ���������� � ����� ���� ��������������� ram-�������������
    with open("materials/prjadm2.xdb", "wb") as f:
        f.write(xml2.toprettyxml(indent="  ", encoding="utf-8"))

print("����������� DBD -> RAM - > XDB2 �������.\n ����� ���� - prjadm2.xdb\n")