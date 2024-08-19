QT += network

HEADERS += \
# Models
    $${PWD}/OAIQuota.h \
    $${PWD}/OAIQuotaList.h \
    $${PWD}/OAIQuotaProperties.h \
    $${PWD}/OAIQuotas_Get_200_response.h \
    $${PWD}/OAIQuotas_List_200_response.h \
    $${PWD}/OAIQuotas_List_200_response_value_inner.h \
    $${PWD}/OAIQuotas_List_200_response_value_inner_properties.h \
# APIs
    $${PWD}/OAIQuotasApi.h \
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
    $${PWD}/OAIQuota.cpp \
    $${PWD}/OAIQuotaList.cpp \
    $${PWD}/OAIQuotaProperties.cpp \
    $${PWD}/OAIQuotas_Get_200_response.cpp \
    $${PWD}/OAIQuotas_List_200_response.cpp \
    $${PWD}/OAIQuotas_List_200_response_value_inner.cpp \
    $${PWD}/OAIQuotas_List_200_response_value_inner_properties.cpp \
# APIs
    $${PWD}/OAIQuotasApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
