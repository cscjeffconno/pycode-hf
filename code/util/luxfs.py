__author__ = 'sancheng'

import argparse
from cmd import Cmd
import glob
import os
import sys


def cmd_ls_parser(cmdline):
    parser = argparse.ArgumentParser()
    parser.add_argument('-S', action='store_true', dest='is_sort_by_size', default=False, help='sort by size')
    parser.add_argument('-t', action='store_true', dest='is_sort_by_time', default=False, help='sort by time')
    parser.add_argument('-r', action='store_true', dest='is_reverse_order', default=False, help='sort in reverse order')
    return parser.parse_args(cmdline.split())


class Simulated_Linux_fs_Cmd(Cmd):
    def __init__(self):
        self.prompt = 'fs>'
        self.path = os.getcwd()
        Cmd.__init__(self, completekey='quit')

    @staticmethod
    def static_mtd(input):
        print 'i am static',input

    def cmdloop(self, intro='a simulated file system command line set under windows'):
        print intro
        Cmd.cmdloop(self)

    def process_one_cmd(self, line):
        pass

    def simple_print(self, file, content):
        if (file is not None):
            cf = open(file, 'a+')
            print >> cf, content
            cf.close()
        else:
            print content

    def cpfile(self, line):
        tokens = line.split()
        dest = tokens[2]
        source = tokens[1]
        if (not os.path.exists(source) or (os.path.isdir(source))):
            print 'source file not found: ', source
        else:
            try:
                newfile = open(dest, 'wb+')
                cfile = open(source, 'r')
                newfile.write(cfile.read())
            finally:
                newfile.close()
                cfile.close()

    def onecmd(self, line):
        try:
            output_to_file = None

            ts = line.split()
            parse_target = line
            #print ts
            if ('>>' in ts):
                output_to_file = ts[ts.index('>>') + 1].strip()
                parse_target = " ".join(ts[:-2])
                #print parse_target

            #interpret commands
            if (line.startswith('ls ') or line == 'ls'):
                import operator

                ls_namespace = None
                if (len(parse_target) >= 4):
                    ls_namespace = cmd_ls_parser(parse_target[3:])
                #print ls_namespace.is_sort_by_size, ls_namespace.is_sort_by_time, ls_namespace.is_reverse_order
                #print self.path

                flist = glob.glob(self.path + "/*")
                sortedlist = [[os.path.basename(os.path.normpath(fn)), os.path.getsize(fn), os.path.getmtime(fn)] for fn
                              in flist]
                if (ls_namespace is not None):
                    rawlist = sortedlist

                    if (ls_namespace.is_sort_by_size):
                        if (ls_namespace.is_reverse_order):
                            sortedlist = sorted(rawlist, key=operator.itemgetter(1), reverse=True)
                        else:
                            sortedlist = sorted(rawlist, key=operator.itemgetter(1), reverse=False)

                    if (ls_namespace.is_sort_by_time):
                        if (ls_namespace.is_reverse_order):
                            sortedlist = sorted(rawlist, key=operator.itemgetter(2), reverse=True)
                        else:
                            sortedlist = sorted(rawlist, key=operator.itemgetter(2), reverse=False)

                for f in sortedlist:
                    #fname = os.path.basename(os.path.normpath(f))

                    self.simple_print(output_to_file, ",".join([str(x) for x in f]))
                print '\r\n'

            if (line.startswith('cd ')):
                tokens = line.split()
                if (not os.path.exists(tokens[1])):
                    self.simple_print(output_to_file, 'path not existed\r\n')
                else:
                    self.path = tokens[1]

            if (line.startswith('cp ')):
                tokens = line.split()
                dest = tokens[2]
                source = tokens[1]
                if (not os.path.exists(source) or (os.path.isdir(source))):
                    print 'source file not found: ', source
                else:
                    try:
                        newfile = open(dest, 'wb+')
                        cfile = open(source, 'r')
                        newfile.write(cfile.read())
                    finally:
                        newfile.close()
                        cfile.close()

            if (line.startswith('head ')):
                headparser = argparse.ArgumentParser()
                headparser.add_argument('-n', dest='hline')
                headparser.add_argument('-b', dest='hb')
                f = parse_target.split()[-1:][0]
                head_option = headparser.parse_args(parse_target[5:].split()[:-1])
                #print head_option.hline, head_option.hb, f
                if (not os.path.exists(f)):
                    return

                if (head_option.hline is not None):
                    #read line file
                    fr = open(f, 'r')
                    #print 'debug'

                    rlist = [fr.readline() for i in range(0, int(head_option.hline))]

                    self.simple_print(output_to_file, "".join(rlist))

                    fr.close()

                elif (head_option.hb is not None):
                    fr = open(f, 'rb')
                    bytes_to_read = int(head_option.hb)
                    #for i in range(0,int(head_option.hb)):
                    b = fr.read(bytes_to_read)
                    #fr.read(n)
                    readstr = None
                    try:
                        readstr = b.decode('ascii')
                    except:
                        try:
                            readstr = b.decode('utf-8')
                        except:
                            readstr = b.decode('gb2312')
                    finally:
                        pass

                    if (readstr is not None):
                        self.simple_print(output_to_file, readstr)
                    fr.close()

            if (line.startswith('rm ')):
                os.remove(line.split()[-1].strip())

            if (line.startswith('mv ')):
                self.cpfile(line)
                os.remove(line.split()[1].strip())

            if(line.startswith('find ')):
                flist = glob.glob1(self.path,line.split()[-1].strip())
                for f in flist:
                    self.simple_print(output_to_file,f)

        except WindowsError, e:
            print sys.exc_info()[0]
            pass
        except:
            print sys.exc_info()[0]
            print 'bad command', line


            # let the quit end the interpreter

    def postcmd(self, stop, line):
        if (line == 'quit'):
            return True


interpreter = Simulated_Linux_fs_Cmd()
#interpreter.cmdloop()
Simulated_Linux_fs_Cmd.static_mtd('aaaa')