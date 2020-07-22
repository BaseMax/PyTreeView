# coding=utf8
# Max Base
# github.com/basemax/pyTree
class pyTree():
    offset=0
    lines={}
    def parse(self, items):
        # global offset#, lines
        # if 'lines' in locals():
        #     self.lines={}
        start=0
        result=[]
        if isinstance(items, list):
            items={v: k for v, k in enumerate(items)}
        # print(items)
        dictPosition=1
        dictSize=len(items)
        for attr, value in items.items():
            result.append([self.offset, '', '', {}])
            if dictPosition == dictSize:
                result[-1][1]='└─'
                # if self.offset in self.lines:
                #     self.lines[self.offset]=self.lines[self.offset] + [len(result)]
                # else:
                #     self.lines.update({self.offset : [len(result)]})
                self.lines[self.offset]=len(result)
                # print("add", self.lines)
            else:
                result[-1][1]='├─'
                # self.lines.update({self.offset : [len(result)]})
                # print(self.lines, self.offset)
                if self.offset in self.lines:
                    del self.lines[self.offset]
            result[-1][2]=str(attr)
            result[-1][3]=self.lines.copy()
            if value == [] or value == {}:
                result[-1][2]+=': []'
            elif isinstance(value, list) or isinstance(value, dict):
                start=len(result)
                self.offset=self.offset+1
                result = result + self.parse(value)
                self.offset=self.offset-1
            else:
                result[-1][2]+=': '+str(value)
            dictPosition+=1
        return result

    def display(self, result):
        result=self.get(result)
        if result[-1] == '\n':
            result=result[:-1]
        print(result)

    def get(self, result):
        answer=''
        tree=self.parse(result)
        # print(tree)
        # for v in tree:
        #     print(v)
        # print(self.lines)
        i=0
        for v in tree:
            result=''
            if v[0] != 0:
                for i in range(v[0]):
                    # print(self.lines[i])
                    if i not in v[3]:
                        result+='│  '
                    else:
                        result+='   '
            else:
                result+=v[0]*'   '
            result+=v[1]+' '+v[2]
            # print(result)
            answer+=result+'\n'
            i+=1
        return answer
