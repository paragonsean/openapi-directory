QT += network

HEADERS += \
# Models
    $${PWD}/OAIAPIError.h \
    $${PWD}/OAIAPIError_errors_inner.h \
    $${PWD}/OAIAuthorizationError.h \
    $${PWD}/OAIVeteranStatusConfirmation.h \
    $${PWD}/OAIVeteranStatusRequest.h \
# APIs
    $${PWD}/OAIVeteranConfirmationStatusApi.h \
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
    $${PWD}/OAIAPIError.cpp \
    $${PWD}/OAIAPIError_errors_inner.cpp \
    $${PWD}/OAIAuthorizationError.cpp \
    $${PWD}/OAIVeteranStatusConfirmation.cpp \
    $${PWD}/OAIVeteranStatusRequest.cpp \
# APIs
    $${PWD}/OAIVeteranConfirmationStatusApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
