QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAILoginRequest.h \
    $${PWD}/OAILogoutresponse.h \
    $${PWD}/OAIServiceTicket.h \
    $${PWD}/OAISession.h \
    $${PWD}/OAISessionsErrors.h \
    $${PWD}/OAITicketvalidityresponse.h \
# APIs
    $${PWD}/OAISessionsApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAILoginRequest.cpp \
    $${PWD}/OAILogoutresponse.cpp \
    $${PWD}/OAIServiceTicket.cpp \
    $${PWD}/OAISession.cpp \
    $${PWD}/OAISessionsErrors.cpp \
    $${PWD}/OAITicketvalidityresponse.cpp \
# APIs
    $${PWD}/OAISessionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
