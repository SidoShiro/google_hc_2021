def write_result(file_name, list_intersection: [], list_streets: [], list_cars: []):
    f_out = open(file_name, 'rw')

    f_out.write(str(len(list_intersection)))

    for c_inter in list_intersection:
        f_out.write(c_inter.inter_id)
        f_out.write(str(c_inter.scheduler))
        for sch in c_inter.scheduler:
            f_out.write(list_streets[sch[0]].street_id + " " + str(sch[1]))

    f_out.close()
