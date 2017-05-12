import search

# Alumno: Alejandro Curbelo Fontelos

travel = search.GPSProblem('A', 'B', search.romania)
# travel = search.GPSProblem('O', 'N', search.romania)
# travel = search.GPSProblem('S', 'B', search.romania)
# travel = search.GPSProblem('G', 'C', search.romania)

print "Busqueda en anchura"
print search.breadth_first_graph_search(travel).path()
print
print "Busqueda en profudidad"
print search.depth_first_graph_search(travel).path()
print
print "Busqueda por ramificacion acotacion"
print search.branch_bound_tree_search(travel).path()
print
print "Busqueda por ramificacion y acotacion con subestimacion"
print search.branch_bound_heuris_tree_search(travel).path()
# print search.iterative_deepening_search(travel).path()
# print search.depth_limited_search(travel).path()

# saq = search.GPSProblem('SA', 'Q', search.australia)

# print search.breadth_first_graph_search(saq).path()
# print search.depth_first_graph_search(saq).path()
# print search.branch_sized_graph_search(saq).path()

#print search.astar_search(travel).path()
