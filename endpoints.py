
class Endpoints:
    login_courier = '/api/v1/courier/login'
    create_courier = '/api/v1/courier'
    delete_courier = '/api/v1/courier/'

    get_order_count_courier = '/api/v1/courier/:id/ordersCount'

    finish_order = '/api/v1/orders/finish/'
    cancel_order = '/api/v1/orders/cancel'
    get_list_order = '/api/v1/orders'
    get_orders_track = '/api/v1/orders/track'
    accept_order = '/api/v1/orders/accept/:id'
    create_order = '/api/v1/orders'