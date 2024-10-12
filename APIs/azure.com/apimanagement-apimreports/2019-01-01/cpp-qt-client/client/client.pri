QT += network

HEADERS += \
# Models
    $${PWD}/OAIReports_ListByApi_200_response.h \
    $${PWD}/OAIReports_ListByApi_200_response_value_inner.h \
    $${PWD}/OAIReports_ListByRequest_200_response.h \
    $${PWD}/OAIReports_ListByRequest_200_response_value_inner.h \
# APIs
    $${PWD}/OAIReportsApi.h \
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
    $${PWD}/OAIReports_ListByApi_200_response.cpp \
    $${PWD}/OAIReports_ListByApi_200_response_value_inner.cpp \
    $${PWD}/OAIReports_ListByRequest_200_response.cpp \
    $${PWD}/OAIReports_ListByRequest_200_response_value_inner.cpp \
# APIs
    $${PWD}/OAIReportsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
