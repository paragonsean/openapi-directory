QT += network

HEADERS += \
# Models
    $${PWD}/OAIAirtravelMultilegRequest.h \
    $${PWD}/OAILeg1.h \
# APIs
    $${PWD}/OAIAirtravelCoordinatesApi.h \
    $${PWD}/OAIAirtravelMultilegApi.h \
    $${PWD}/OAIEcommerceDeliveryApi.h \
    $${PWD}/OAIRequestApiKeyApi.h \
    $${PWD}/OAIRoadDistanceApi.h \
    $${PWD}/OAIUrbanDeliveryApi.h \
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
    $${PWD}/OAIAirtravelMultilegRequest.cpp \
    $${PWD}/OAILeg1.cpp \
# APIs
    $${PWD}/OAIAirtravelCoordinatesApi.cpp \
    $${PWD}/OAIAirtravelMultilegApi.cpp \
    $${PWD}/OAIEcommerceDeliveryApi.cpp \
    $${PWD}/OAIRequestApiKeyApi.cpp \
    $${PWD}/OAIRoadDistanceApi.cpp \
    $${PWD}/OAIUrbanDeliveryApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
