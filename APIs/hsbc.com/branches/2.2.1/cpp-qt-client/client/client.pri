QT += network

HEADERS += \
# Models
    $${PWD}/OAIBranchDefinition.h \
    $${PWD}/OAIBranchDefinitionMeta.h \
    $${PWD}/OAIBranch_inner.h \
    $${PWD}/OAIBrand_inner.h \
    $${PWD}/OAIContactInfo_inner.h \
    $${PWD}/OAIErrorDefinition400.h \
    $${PWD}/OAIErrorDefinition408.h \
    $${PWD}/OAIErrorDefinition429.h \
    $${PWD}/OAIErrorDefinition500.h \
    $${PWD}/OAIErrorDefinition503.h \
    $${PWD}/OAIMetaDefinition.h \
    $${PWD}/OAIOtherAccessibility_inner.h \
    $${PWD}/OAIOtherCustomerSegment_inner.h \
    $${PWD}/OAIOtherServiceAndFacility_inner.h \
# APIs
    $${PWD}/OAIBranchesApi.h \
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
    $${PWD}/OAIBranchDefinition.cpp \
    $${PWD}/OAIBranchDefinitionMeta.cpp \
    $${PWD}/OAIBranch_inner.cpp \
    $${PWD}/OAIBrand_inner.cpp \
    $${PWD}/OAIContactInfo_inner.cpp \
    $${PWD}/OAIErrorDefinition400.cpp \
    $${PWD}/OAIErrorDefinition408.cpp \
    $${PWD}/OAIErrorDefinition429.cpp \
    $${PWD}/OAIErrorDefinition500.cpp \
    $${PWD}/OAIErrorDefinition503.cpp \
    $${PWD}/OAIMetaDefinition.cpp \
    $${PWD}/OAIOtherAccessibility_inner.cpp \
    $${PWD}/OAIOtherCustomerSegment_inner.cpp \
    $${PWD}/OAIOtherServiceAndFacility_inner.cpp \
# APIs
    $${PWD}/OAIBranchesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
