import os
from lizaliblove.main import draw_ast


def generate_begin():
    return "\\documentclass{article}\n\\usepackage{graphicx}\\usepackage[utf8]{inputenc}\n" + \
           "\\begin{document}\n\\begin{center}"


def generate_end():
    return "\\end{center}\\end{document}"


def generate_table(table_generated):
    return "\\begin{tabular}{" + "l" * len(table_generated[0]) + "}\n" + \
           "\\\\\n".join(map(lambda line: "&".join(line), table_generated)) + \
           "\n\\end{tabular}" + "\n"


def generate_image(path_to_img):
    draw_ast()
    return f"\\includegraphics[width=\\textwidth]{{{path_to_img}}}\n"


def generate_tex(table_generated, path_to_img):
    return ''.join([generate_begin(), generate_table(table_generated), generate_image(path_to_img), generate_end()
                    ])


if __name__ == '__main__':
    table = [["python", "java", "c", "r"], ["kekkkkekeke", "hashhahshsahhsasa",
                                            "mem", "lol"],
             ["3jj3j3j3j3", "shikdkdkkd", "232323233", "ddhdhdhdhdhd2323"]]
    with open("artifacts/table.tex", "w") as file:
        file.write(generate_tex(table, "artifacts/ast.png"))
    os.system(f"pdflatex -output-directory=artifacts artifacts/table.tex")
    os.system(f"rm artifacts/table.aux artifacts/table.log")
