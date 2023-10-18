class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""

        while columnNumber > 0:
            columnNumber -=1 
            title += chr(ord("A") + ( columnNumber ) % 26 )
            columnNumber = columnNumber // 26
        
        return title[::-1]