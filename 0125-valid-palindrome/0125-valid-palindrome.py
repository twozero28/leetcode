class Solution(object):
    def isPalindrome(self, s):
        extracted_str = ''.join(re.findall('[a-zA-Z0-9]', s)).lower()
        
        return extracted_str == extracted_str[::-1]
        