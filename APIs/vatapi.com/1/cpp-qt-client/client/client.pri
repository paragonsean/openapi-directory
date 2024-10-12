QT += network

HEADERS += \
# Models
    $${PWD}/OAIApi_Usage.h \
    $${PWD}/OAIConvert_Price.h \
    $${PWD}/OAICountry_Code_Check.h \
    $${PWD}/OAICountry_Data.h \
    $${PWD}/OAICountry_Rates.h \
    $${PWD}/OAICreate_Invoice.h \
    $${PWD}/OAICurrency_Conversion.h \
    $${PWD}/OAIIP_Check.h \
    $${PWD}/OAIInvoice_Array.h \
    $${PWD}/OAIInvoice_Data.h \
    $${PWD}/OAIInvoice_Items.h \
    $${PWD}/OAIParking.h \
    $${PWD}/OAIReduced.h \
    $${PWD}/OAIReduced_alt.h \
    $${PWD}/OAIRetrieve_Invoice.h \
    $${PWD}/OAIRetrieve_Invoice_Array.h \
    $${PWD}/OAIStandard.h \
    $${PWD}/OAISuper_reduced.h \
    $${PWD}/OAIUpdate_Invoice.h \
    $${PWD}/OAIUpdate_Invoice_Array.h \
    $${PWD}/OAIVat_Rates.h \
    $${PWD}/OAIVat_Rates_Countries.h \
# APIs
    $${PWD}/OAIApiApi.h \
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
    $${PWD}/OAIApi_Usage.cpp \
    $${PWD}/OAIConvert_Price.cpp \
    $${PWD}/OAICountry_Code_Check.cpp \
    $${PWD}/OAICountry_Data.cpp \
    $${PWD}/OAICountry_Rates.cpp \
    $${PWD}/OAICreate_Invoice.cpp \
    $${PWD}/OAICurrency_Conversion.cpp \
    $${PWD}/OAIIP_Check.cpp \
    $${PWD}/OAIInvoice_Array.cpp \
    $${PWD}/OAIInvoice_Data.cpp \
    $${PWD}/OAIInvoice_Items.cpp \
    $${PWD}/OAIParking.cpp \
    $${PWD}/OAIReduced.cpp \
    $${PWD}/OAIReduced_alt.cpp \
    $${PWD}/OAIRetrieve_Invoice.cpp \
    $${PWD}/OAIRetrieve_Invoice_Array.cpp \
    $${PWD}/OAIStandard.cpp \
    $${PWD}/OAISuper_reduced.cpp \
    $${PWD}/OAIUpdate_Invoice.cpp \
    $${PWD}/OAIUpdate_Invoice_Array.cpp \
    $${PWD}/OAIVat_Rates.cpp \
    $${PWD}/OAIVat_Rates_Countries.cpp \
# APIs
    $${PWD}/OAIApiApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
