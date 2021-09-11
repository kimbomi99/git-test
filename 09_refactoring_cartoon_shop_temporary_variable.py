import math

input_cartoon_info = {
    "진격의거인": {"name": "진격의 거인", "genre": "판타지"},
    "원피스": {"name": "원피스", "genre": "소년만화"},
    "짱구": {"name": "짱구는 못말려", "genre": "코믹"},
    "괴짜가족": {"name": "괴짜 가족", "genre": "코믹"},
}

input_order_histories = [
    {
        "customer": "의정부고",
        "cartoon_consumption_histories":
            [
                {
                    "cartoon_id": "진격의거인", "view_count": 55
                },
                {
                    "cartoon_id": "원피스", "view_count": 40
                },
                {
                    "cartoon_id": "짱구", "view_count": 20
                },
                {
                    "cartoon_id": "괴짜가족", "view_count": 15
                }
            ]
    },
    {
        "customer": "의여고",
        "cartoon_consumption_histories":
            [
                {
                    "cartoon_id": "진격의거인", "view_count": 20
                },
                {
                    "cartoon_id": "원피스", "view_count": 10
                },
                {
                    "cartoon_id": "짱구", "view_count": 50
                },
                {
                    "cartoon_id": "괴짜가족", "view_count": 60
                }
            ]
    },
]


def get_result(order_histories, cartoon_info):
    return get_output_data(get_order_data_list(cartoon_info, order_histories))


def get_order_data_list(cartoon_info, order_histories):
    order_data_list = []
    for order_history in order_histories:
        cartoon_consumption_histories = []
        for cartoon_consumption_history in order_history["cartoon_consumption_histories"]:
            cartoon_consumption_histories.append({
                "cartoon_name": get_cartoon(cartoon_consumption_history, cartoon_info)['name'],
                "amount": calculate_cost_of_comic(get_cartoon(cartoon_consumption_history, cartoon_info),
                                                  cartoon_consumption_history),
                "view_count": cartoon_consumption_history['view_count']
            })

        order_data_list.append({
            "customer": order_history["customer"],
            "total_amount": calculate_total_amount_from_histories(cartoon_info, order_history),
            "point": calculate_point_from_histories(cartoon_info, order_history),
            "cartoon_consumption_histories": cartoon_consumption_histories
        })
    return order_data_list