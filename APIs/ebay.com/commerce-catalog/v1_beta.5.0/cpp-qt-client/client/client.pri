QT += network

HEADERS += \
# Models
    $${PWD}/OAIAspect.h \
    $${PWD}/OAIAspectDistribution.h \
    $${PWD}/OAIAspectValueDistribution.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIImage.h \
    $${PWD}/OAIProduct.h \
    $${PWD}/OAIProductSearchResponse.h \
    $${PWD}/OAIProductSummary.h \
    $${PWD}/OAIRefinement.h \
# APIs
    $${PWD}/OAIProductApi.h \
    $${PWD}/OAIProductSummaryApi.h \
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
    $${PWD}/OAIAspect.cpp \
    $${PWD}/OAIAspectDistribution.cpp \
    $${PWD}/OAIAspectValueDistribution.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIImage.cpp \
    $${PWD}/OAIProduct.cpp \
    $${PWD}/OAIProductSearchResponse.cpp \
    $${PWD}/OAIProductSummary.cpp \
    $${PWD}/OAIRefinement.cpp \
# APIs
    $${PWD}/OAIProductApi.cpp \
    $${PWD}/OAIProductSummaryApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
