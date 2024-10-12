QT += network

HEADERS += \
# Models
    $${PWD}/OAIIssue_ListByService_200_response.h \
    $${PWD}/OAIIssue_ListByService_200_response_value_inner.h \
    $${PWD}/OAIIssue_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAIIssue_ListByService_default_response.h \
    $${PWD}/OAIIssue_ListByService_default_response_error.h \
    $${PWD}/OAIIssue_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAIIssuesApi.h \
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
    $${PWD}/OAIIssue_ListByService_200_response.cpp \
    $${PWD}/OAIIssue_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAIIssue_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAIIssue_ListByService_default_response.cpp \
    $${PWD}/OAIIssue_ListByService_default_response_error.cpp \
    $${PWD}/OAIIssue_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAIIssuesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
