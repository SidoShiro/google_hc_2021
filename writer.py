def write_result(file_name, list_intersection: [], list_streets: [], list_cars: []):
    f_out = open(file_name, 'w')

    f_out.write(str(len(list_intersection)) + '\n')

    for c_inter in list_intersection:
        f_out.write(str(c_inter.inter_id) + '\n')
        f_out.write(str(len(c_inter.scheduler)) + '\n')
        for sch in c_inter.scheduler:
            f_out.write(sch[0] + " " + str(sch[1]) + '\n')

    f_out.close()
