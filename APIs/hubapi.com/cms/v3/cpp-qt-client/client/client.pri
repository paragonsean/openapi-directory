QT += network

HEADERS += \
# Models
    $${PWD}/OAICollectionResponseWithTotalDomainForwardPaging.h \
    $${PWD}/OAIDomain.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIForwardPaging.h \
    $${PWD}/OAINextPage.h \
# APIs
    $${PWD}/OAIDomainsApi.h \
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
    $${PWD}/OAICollectionResponseWithTotalDomainForwardPaging.cpp \
    $${PWD}/OAIDomain.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIForwardPaging.cpp \
    $${PWD}/OAINextPage.cpp \
# APIs
    $${PWD}/OAIDomainsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
