QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessLevel.h \
    $${PWD}/OAIAccessPolicy.h \
    $${PWD}/OAIBasicLevel.h \
    $${PWD}/OAICondition.h \
    $${PWD}/OAICustomLevel.h \
    $${PWD}/OAIDevicePolicy.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIListAccessLevelsResponse.h \
    $${PWD}/OAIListAccessPoliciesResponse.h \
    $${PWD}/OAIListServicePerimetersResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOsConstraint.h \
    $${PWD}/OAIServicePerimeter.h \
    $${PWD}/OAIServicePerimeterConfig.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIVpcAccessibleServices.h \
# APIs
    $${PWD}/OAIAccessPoliciesApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIAccessLevel.cpp \
    $${PWD}/OAIAccessPolicy.cpp \
    $${PWD}/OAIBasicLevel.cpp \
    $${PWD}/OAICondition.cpp \
    $${PWD}/OAICustomLevel.cpp \
    $${PWD}/OAIDevicePolicy.cpp \
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIListAccessLevelsResponse.cpp \
    $${PWD}/OAIListAccessPoliciesResponse.cpp \
    $${PWD}/OAIListServicePerimetersResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOsConstraint.cpp \
    $${PWD}/OAIServicePerimeter.cpp \
    $${PWD}/OAIServicePerimeterConfig.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIVpcAccessibleServices.cpp \
# APIs
    $${PWD}/OAIAccessPoliciesApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
