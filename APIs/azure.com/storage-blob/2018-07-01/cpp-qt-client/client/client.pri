QT += network

HEADERS += \
# Models
    $${PWD}/OAIBlobContainer.h \
    $${PWD}/OAIBlobServiceProperties.h \
    $${PWD}/OAIContainerProperties.h \
    $${PWD}/OAICorsRule.h \
    $${PWD}/OAICorsRules.h \
    $${PWD}/OAIDeleteRetentionPolicy.h \
    $${PWD}/OAIImmutabilityPolicy.h \
    $${PWD}/OAIImmutabilityPolicyProperties.h \
    $${PWD}/OAIImmutabilityPolicyProperty.h \
    $${PWD}/OAILeaseContainerRequest.h \
    $${PWD}/OAILeaseContainerResponse.h \
    $${PWD}/OAILegalHold.h \
    $${PWD}/OAILegalHoldProperties.h \
    $${PWD}/OAIListContainerItem.h \
    $${PWD}/OAIListContainerItems.h \
    $${PWD}/OAITagProperty.h \
    $${PWD}/OAIUpdateHistoryProperty.h \
# APIs
    $${PWD}/OAIBlobContainersApi.h \
    $${PWD}/OAIBlobServiceApi.h \
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
    $${PWD}/OAIBlobContainer.cpp \
    $${PWD}/OAIBlobServiceProperties.cpp \
    $${PWD}/OAIContainerProperties.cpp \
    $${PWD}/OAICorsRule.cpp \
    $${PWD}/OAICorsRules.cpp \
    $${PWD}/OAIDeleteRetentionPolicy.cpp \
    $${PWD}/OAIImmutabilityPolicy.cpp \
    $${PWD}/OAIImmutabilityPolicyProperties.cpp \
    $${PWD}/OAIImmutabilityPolicyProperty.cpp \
    $${PWD}/OAILeaseContainerRequest.cpp \
    $${PWD}/OAILeaseContainerResponse.cpp \
    $${PWD}/OAILegalHold.cpp \
    $${PWD}/OAILegalHoldProperties.cpp \
    $${PWD}/OAIListContainerItem.cpp \
    $${PWD}/OAIListContainerItems.cpp \
    $${PWD}/OAITagProperty.cpp \
    $${PWD}/OAIUpdateHistoryProperty.cpp \
# APIs
    $${PWD}/OAIBlobContainersApi.cpp \
    $${PWD}/OAIBlobServiceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
