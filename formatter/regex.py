LINE_COMMENT = r'\s*\/\/'

WHILE = r'(^|\s+|;|{|})while\s*(\(|\n)'
FOR = r'(^|\s+|;|{|})for\s*(\(|\n)'
IF = r'(^|\s+|;|{|})if\s*(\(|\n)'
ELSE = r'(^|\s+|;|{|})else(\s+|\s*(\n|{))'
SWITCH = r'(^|\s+|;|{|})switch\s*(\(|\n)'
TRY_RESOURCES = r'(^|\s+|;|{|})try\s*(\(|\n)'

CLOSING_BRACE = r'(^|\s*)}'
DEFAULT = r'(^|\s+|;|{|})default\s*(:|\n)'

#acess modifiers
MODIFIER = r'(^|\s+)(public|private|protected|privileged)(\n|\s+)'


REPLACE_MULTIPLE_SPACES = r'(\s+(?=\(|\)|=|&|\^|!|\+|-|\*|\/|%|>|<|\||~|\?|:|\.|;|{|})' \
                          r'|((?<=\(|\)|=|&|\^|!|\+|-|\*|\/|%|>|<|\||~|\?|:|\.|;|{|})\s+))'
OPERATOR_NOT = r'((?<=[^+\-\*\/%<>\^!])|(?<=^))!(?=([^=+\-<>&\|]|$))'

#unary operators
OPERATOR_UNARY_NEGATION = r'((?<=[=\+\*\/%<>\^!&\|\(\)\[ ])|(?<=^))-(?=([^=+\-<>&\|]|$))'
OPERATOR_UNARY_PLUS = r'((?<=[=\-\*\/%<>\^!&\|\(\)\[ ])|(?<=^))\+(?=([^=+\-<>&\|]|$))'

WRAP_KEYWORD = r'(?<=(\)|\s))KEYWORD\s+'
WRAP_LINE = r'(?<=(\)|\s))LINE\s+'
BLANK_LINES_PACKAGE = r'\s*package\s'
BLANK_LINES_IMPORT = r'\s*import\s'
