# Contexts
def math():
	return vim.eval('vimtex#syntax#in_mathzone()') == '1'

def comment():
	return vim.eval('vimtex#syntax#in_comment()') == '1'

def env(name):
	[x,y] = vim.eval("vimtex#env#is_inside('" + name + "')")
	return x != '0' and y != '0'


# Utils

def complete(t, opts):
  if t:
    opts = [m[len(t):] for m in opts if m.startswith(t)]
  if len(opts) == 0:
    return ''
  elif len(opts) == 1:
    return opts[0]
  else:
    return '(' + '|'.join(opts) + ')'

def create_row_placeholders(snip):
    # retrieving single line from current string and treat it like tabstops
    # count
    placeholders_amount = int(snip.buffer[snip.line].strip())

    # erase current line
    snip.buffer[snip.line] = ''

    # create anonymous snippet with expected content and number of tabstops
    anon_snippet_body = ' & '.join(['$' + str(i+1) for i in range(placeholders_amount)])

    # expand anonymous snippet
    snip.expand_anon(anon_snippet_body)


def create_table(snip):
	rows = snip.buffer[snip.line].split('x')[0]
	cols = snip.buffer[snip.line].split('x')[1]
	int_val = lambda string: int(''.join(s for s in string if s.isdigit()))
	rows = int_val(rows)
	cols = int_val(cols)
	offset = cols + 1
	old_spacing = snip.buffer[snip.line][:snip.buffer[snip.line].rfind('\t') + 1]
	snip.buffer[snip.line] = ''
	final_str = old_spacing + "\\begin{tabular}{|" + "|".join(['$' + str(i + 1) for i in range(cols)]) + "|}\n"
	for i in range(rows):
		final_str += old_spacing + '\t'
		final_str += " & ".join(['$' + str(i * cols + j + offset) for j in range(cols)])
		final_str += " \\\\\\\n"
	final_str += old_spacing + "\\end{tabular}\n$0"
	snip.expand_anon(final_str)
def add_row(snip):
	row_len = int(''.join(s for s in snip.buffer[snip.line] if s.isdigit()))
	old_spacing = snip.buffer[snip.line][:snip.buffer[snip.line].rfind('\t') + 1]
	snip.buffer[snip.line] = ''
	final_str = old_spacing
	final_str += " & ".join(['$' + str(j + 1) for j in range(row_len)])
	final_str += " \\\\\\"
	snip.expand_anon(final_str)

def create_matrix_placeholders(snip):
	# Create anonymous snippet body
	anon_snippet_body = ""

	# Get start and end line number of expanded snippet
	start = snip.snippet_start[0]
	end = snip.snippet_end[0]

  # Append current line into anonymous snippet
	for i in range(start, end + 1):
		anon_snippet_body += snip.buffer[i]
		anon_snippet_body += "" if i == end else "\n"

	# Delete expanded snippet line till second to last line
	for i in range(start, end):
		del snip.buffer[start]

	# Empty last expanded snippet line while preserving the line
	snip.buffer[start] = ''

	# Expand anonymous snippet
	snip.expand_anon(anon_snippet_body)

def create_matrix(cols, rows, sep, start, end):
	res = ""
	placeholder = 1
	for _ in range(0, int(rows)):
		res += start + f"${placeholder} "
		placeholder += 1
		for _ in range(0, int(cols) - 1):
			res += sep + f" ${placeholder} "
			placeholder += 1
		res += end
	return res[:-1]


