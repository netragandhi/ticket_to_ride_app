import cv2 as cv
from detect_pieces import align_images, match_images, analyze_routes, visualize_segments
from game_logic import build_adj_list, calculate_ticket_points, calculate_route_points, calculate_total_points

empty_img = cv.imread('imgs/empty.jpeg')
played_img = cv.imread('imgs/played.jpeg')

aligned = align_images(empty_img, played_img)
matched = match_images(empty_img, aligned)
# diff_vis = cv.absdiff(aligned, matched)
# cv.imshow("Normalization Difference", diff_vis)
route_owners, results = analyze_routes(empty_img, matched)

# neighbors = build_adj_list(route_owners)
neighbors = {
    "blue": {
        "bangkok": {"hongkong", "jakarta"},
        "jakarta": {"darwin", "bangkok"},
        "darwin": {"jakarta"},
        "hongkong": {"bangkok", "manila"},
        "manila": {"hongkong", "tokyo"},
        "tokyo": {"manila"}
    } # make a fake route
}

tickets = {"blue": {"bangkok_tokyo", "miami_buenosaires"}} # user input (will make this cv eventually)

total_ticket_points = calculate_ticket_points(tickets, neighbors)
print(total_ticket_points)

total_route_points = calculate_route_points(route_owners)
print(total_route_points)

print(calculate_total_points(tickets, neighbors, route_owners))

# for route, segs in results.items():
#     print(f"\nRoute: {route}")
#     for i, s in enumerate(segs):
#         print(f" Segment {i}: hue={s['hue']}, value={s['value']}, occupied={s['occupied']}, ")
            #   f"color_diff={s['color_diff']:.2f}, edge_diff={s['edge_diff']:.2f}, "
            #   f"tex_diff={s['tex_diff']:.2f}, reason={s['reason']}")

# visualize_segments(empty_img, matched, results)