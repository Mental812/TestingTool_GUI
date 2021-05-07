import time,os
class libStorageClass():
    def __init__(self):
        self.__testfile_location = "/home/nvidia/testfile"

    def test_storage(self,device_name):
        try:
            os.system("sudo umount /mnt")       
            os.system("sudo mount {device} /mnt".format(device = device_name))
            os.system("sudo dd if=/dev/zero of={flocation} bs=1024 count=1024000".format(flocation = self.__testfile_location))
            start_time = time.time()
            os.system("cp {flocation} /mnt".format(flocation = self.__testfile_location))
            end_time = time.time()
            file_size = os.stat('/mnt/testfile').st_size/1000000
            speed = (file_size)/(end_time- start_time)
            print(speed,"MB/s")


            os.system("sudo rm {flocation}".format(flocation = self.__testfile_location))
            os.system("sudo rm /mnt/testfile")
            if speed != 0:
                return True
            else:
        except Exception as e:
            print(e)
            return False