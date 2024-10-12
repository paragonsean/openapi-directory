QT += network

HEADERS += \
# Models
    $${PWD}/OAIAbuseTicket.h \
    $${PWD}/OAIAbuseTicketCreate.h \
    $${PWD}/OAIAbuseTicketId.h \
    $${PWD}/OAIAbuseTicketList.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorField.h \
    $${PWD}/OAIPagination.h \
# APIs
    $${PWD}/OAIV1Api.h \
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
    $${PWD}/OAIAbuseTicket.cpp \
    $${PWD}/OAIAbuseTicketCreate.cpp \
    $${PWD}/OAIAbuseTicketId.cpp \
    $${PWD}/OAIAbuseTicketList.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorField.cpp \
    $${PWD}/OAIPagination.cpp \
# APIs
    $${PWD}/OAIV1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
