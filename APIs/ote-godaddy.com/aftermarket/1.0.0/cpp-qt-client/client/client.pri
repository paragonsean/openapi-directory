QT += network

HEADERS += \
# Models
    $${PWD}/OAIAftermarketListingAction.h \
    $${PWD}/OAIAftermarketListingExpiryCreate.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorField.h \
    $${PWD}/OAIErrorLimit.h \
    $${PWD}/OAIExpiry.h \
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
    $${PWD}/OAIAftermarketListingAction.cpp \
    $${PWD}/OAIAftermarketListingExpiryCreate.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorField.cpp \
    $${PWD}/OAIErrorLimit.cpp \
    $${PWD}/OAIExpiry.cpp \
# APIs
    $${PWD}/OAIV1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
