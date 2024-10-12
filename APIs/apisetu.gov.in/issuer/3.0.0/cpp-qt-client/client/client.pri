QT += network

HEADERS += \
# Models
    $${PWD}/OAIPullDocRequest.h \
    $${PWD}/OAIPullDocRequest_DocDetails.h \
    $${PWD}/OAIPullDocResponse.h \
    $${PWD}/OAIPullDocResponse_DocDetails.h \
    $${PWD}/OAIPullDocResponse_ResponseStatus.h \
    $${PWD}/OAIPullURIRequest.h \
    $${PWD}/OAIPullURIRequest_DocDetails.h \
    $${PWD}/OAIPullURIResponse.h \
    $${PWD}/OAIPullURIResponse_DocDetails.h \
    $${PWD}/OAIPullURIResponse_ResponseStatus.h \
# APIs
    $${PWD}/OAIAPIsApi.h \
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
    $${PWD}/OAIPullDocRequest.cpp \
    $${PWD}/OAIPullDocRequest_DocDetails.cpp \
    $${PWD}/OAIPullDocResponse.cpp \
    $${PWD}/OAIPullDocResponse_DocDetails.cpp \
    $${PWD}/OAIPullDocResponse_ResponseStatus.cpp \
    $${PWD}/OAIPullURIRequest.cpp \
    $${PWD}/OAIPullURIRequest_DocDetails.cpp \
    $${PWD}/OAIPullURIResponse.cpp \
    $${PWD}/OAIPullURIResponse_DocDetails.cpp \
    $${PWD}/OAIPullURIResponse_ResponseStatus.cpp \
# APIs
    $${PWD}/OAIAPIsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
