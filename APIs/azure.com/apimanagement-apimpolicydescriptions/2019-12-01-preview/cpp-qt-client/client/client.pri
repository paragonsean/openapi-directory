QT += network

HEADERS += \
# Models
    $${PWD}/OAIPolicyDescription_ListByService_200_response.h \
    $${PWD}/OAIPolicyDescription_ListByService_200_response_value_inner.h \
    $${PWD}/OAIPolicyDescription_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIPolicyDescription_ListByService_default_response.h \
    $${PWD}/OAIPolicyDescription_ListByService_default_response_error.h \
    $${PWD}/OAIPolicyDescription_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIPolicyDescriptionApi.h \
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
    $${PWD}/OAIPolicyDescription_ListByService_200_response.cpp \
    $${PWD}/OAIPolicyDescription_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIPolicyDescription_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIPolicyDescription_ListByService_default_response.cpp \
    $${PWD}/OAIPolicyDescription_ListByService_default_response_error.cpp \
    $${PWD}/OAIPolicyDescription_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIPolicyDescriptionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
