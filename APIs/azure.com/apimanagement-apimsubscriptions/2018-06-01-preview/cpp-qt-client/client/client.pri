QT += network

HEADERS += \
# Models
    $${PWD}/OAISubscription_CreateOrUpdate_request.h \
    $${PWD}/OAISubscription_CreateOrUpdate_request_properties.h \
    $${PWD}/OAISubscription_Get_200_response.h \
    $${PWD}/OAISubscription_List_200_response.h \
    $${PWD}/OAISubscription_List_200_response_value_inner.h \
    $${PWD}/OAISubscription_List_200_response_value_inner_properties.h \
    $${PWD}/OAISubscription_List_default_response.h \
    $${PWD}/OAISubscription_List_default_response_error.h \
    $${PWD}/OAISubscription_List_default_response_error_details_inner.h \
    $${PWD}/OAISubscription_Update_request.h \
    $${PWD}/OAISubscription_Update_request_properties.h \
# APIs
    $${PWD}/OAISubscriptionApi.h \
    $${PWD}/OAISubscriptionsApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAISubscription_CreateOrUpdate_request.cpp \
    $${PWD}/OAISubscription_CreateOrUpdate_request_properties.cpp \
    $${PWD}/OAISubscription_Get_200_response.cpp \
    $${PWD}/OAISubscription_List_200_response.cpp \
    $${PWD}/OAISubscription_List_200_response_value_inner.cpp \
    $${PWD}/OAISubscription_List_200_response_value_inner_properties.cpp \
    $${PWD}/OAISubscription_List_default_response.cpp \
    $${PWD}/OAISubscription_List_default_response_error.cpp \
    $${PWD}/OAISubscription_List_default_response_error_details_inner.cpp \
    $${PWD}/OAISubscription_Update_request.cpp \
    $${PWD}/OAISubscription_Update_request_properties.cpp \
# APIs
    $${PWD}/OAISubscriptionApi.cpp \
    $${PWD}/OAISubscriptionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
