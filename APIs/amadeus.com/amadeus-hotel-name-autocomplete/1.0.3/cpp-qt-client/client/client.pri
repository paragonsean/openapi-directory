QT += network

HEADERS += \
# Models
    $${PWD}/OAIGethotels_400_response.h \
    $${PWD}/OAIGethotels_400_response_errors_inner.h \
    $${PWD}/OAIGethotels_400_response_errors_inner_source.h \
    $${PWD}/OAIGethotels_500_response.h \
    $${PWD}/OAISuccess.h \
    $${PWD}/OAISuccess_data_inner.h \
    $${PWD}/OAISuccess_data_inner_address.h \
    $${PWD}/OAISuccess_data_inner_geoCode.h \
# APIs
    $${PWD}/OAISearchApi.h \
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
    $${PWD}/OAIGethotels_400_response.cpp \
    $${PWD}/OAIGethotels_400_response_errors_inner.cpp \
    $${PWD}/OAIGethotels_400_response_errors_inner_source.cpp \
    $${PWD}/OAIGethotels_500_response.cpp \
    $${PWD}/OAISuccess.cpp \
    $${PWD}/OAISuccess_data_inner.cpp \
    $${PWD}/OAISuccess_data_inner_address.cpp \
    $${PWD}/OAISuccess_data_inner_geoCode.cpp \
# APIs
    $${PWD}/OAISearchApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
