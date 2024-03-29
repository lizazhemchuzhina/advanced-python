import ast
import inspect
import networkx as nx

from hw_01.src.ast_graph import AstGraph
from hw_01.src.fibonacci import fibonacci

if __name__ == "__main__":
    ast_object = ast.parse(inspect.getsource(fibonacci))
    ast_graph = AstGraph()
    ast_graph.visit(ast_object)
    nx.drawing.nx_pydot.to_pydot(ast_graph.graph).write_png("artifacts/ast.png")
