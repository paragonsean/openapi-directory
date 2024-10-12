QT += network

HEADERS += \
# Models
    $${PWD}/OAIDiscount.h \
    $${PWD}/OAILicense.h \
    $${PWD}/OAILicenseTemplate.h \
    $${PWD}/OAILicensee.h \
    $${PWD}/OAILicensingModel.h \
    $${PWD}/OAINetlicensing.h \
    $${PWD}/OAIPaymentMethod.h \
    $${PWD}/OAIProduct.h \
    $${PWD}/OAIProductModule.h \
    $${PWD}/OAIToken.h \
    $${PWD}/OAITransaction.h \
# APIs
    $${PWD}/OAILicenseApi.h \
    $${PWD}/OAILicenseTemplateApi.h \
    $${PWD}/OAILicenseeApi.h \
    $${PWD}/OAIPaymentMethodApi.h \
    $${PWD}/OAIProductApi.h \
    $${PWD}/OAIProductModuleApi.h \
    $${PWD}/OAITokenApi.h \
    $${PWD}/OAITransactionApi.h \
    $${PWD}/OAIUtilityApi.h \
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
    $${PWD}/OAIDiscount.cpp \
    $${PWD}/OAILicense.cpp \
    $${PWD}/OAILicenseTemplate.cpp \
    $${PWD}/OAILicensee.cpp \
    $${PWD}/OAILicensingModel.cpp \
    $${PWD}/OAINetlicensing.cpp \
    $${PWD}/OAIPaymentMethod.cpp \
    $${PWD}/OAIProduct.cpp \
    $${PWD}/OAIProductModule.cpp \
    $${PWD}/OAIToken.cpp \
    $${PWD}/OAITransaction.cpp \
# APIs
    $${PWD}/OAILicenseApi.cpp \
    $${PWD}/OAILicenseTemplateApi.cpp \
    $${PWD}/OAILicenseeApi.cpp \
    $${PWD}/OAIPaymentMethodApi.cpp \
    $${PWD}/OAIProductApi.cpp \
    $${PWD}/OAIProductModuleApi.cpp \
    $${PWD}/OAITokenApi.cpp \
    $${PWD}/OAITransactionApi.cpp \
    $${PWD}/OAIUtilityApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
