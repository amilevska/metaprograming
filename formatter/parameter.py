import re

class Parameters:

    default_params = {
'tab-size': 4,
'indent-size': 4,
'continuation-indent': 4,
'spaces-before-while': 1,
'spaces-before-for': 1,
'spaces-before-if': 1,
'spaces-before-else': 0,
'spaces-before-try': 1,
'spaces-before-catch': 1,
'spaces-before-method-call': 0,
'spaces-around-assign': 1,
'spaces-around-equal': 1,
'spaces-around-add': 1,
'spaces-around-multiplicate': 1,
'spaces-before-line-comment-after-code': 1,
'braces-placement-class': 'end-of-line',
'braces-placement-method': 'end-of-line',
'braces-placement-other': 'end-of-line',
'keyword-on-new-line-else': 0,
'keyword-on-new-line-while': 1,
'keyword-on-new-line-catch': 0,
'keyword-on-new-line-switch': 0,
'wrap-keyword-extends': 0,
'wrap-keyword-implements': 0,
'wrap-keyword-throws': 0,
'wrap-list-extends': 0,
'wrap-list-implements': 0,
'wrap-list-throws': 0,
'keep-max-blank-lines': 2,
'blank-lines-min-before-package': 0,
'blank-lines-min-before-imports': 1,
'blank-lines-min-before-class-definition': 0,
'blank-lines-min-after-package': 1,
'blank-lines-min-after-imports': 1,
'blank-lines-min-after-class-end': 1,
    }

    params = dict()

    def tab_size(self):
        return int(self.params['tab-size'])

    def indent_size(self):
        return int(self.params['indent-size'])

    def approve_braces_placement(self, value):
        if value not in ['end-of-line', 'new-line', 'new-line-shifted']:
            value = 'end-of-line'
        return value

    def approve_number(self, value):
        if int(value) < 0:
            return 0
        return int(value)

    def __init__(self, filename=''):
        # Initialize params with default values
        self.params = self.default_params


f = open(filename, 'r')
for line in f.readlines():
            if not line.startswith("#") and ":" in line:
                search = re.match(r'.*(?=:\s*)', line)
                if search is not None:
                    value = line[search.end():].replace(':', '').replace(' ', '').replace('\n', '')
                    if search.group() in ['braces-placement-class', 'braces-placement-method', 'braces-placement-other']:
                        value = self.approve_braces_placement(value)
                    elif search.group() != 'keep-max-blank-lines':
                        value = self.approve_number(value)
                self.params[search.group()] = value

