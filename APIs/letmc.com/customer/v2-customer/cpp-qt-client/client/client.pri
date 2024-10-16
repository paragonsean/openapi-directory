QT += network

HEADERS += \
# Models
    $${PWD}/OAIBranchModel.h \
    $${PWD}/OAIBranchModelResults.h \
    $${PWD}/OAIKeyValuePair_String_String_.h \
    $${PWD}/OAILandlordAccountingEntryModel.h \
    $${PWD}/OAILandlordAccountingInvoiceModel.h \
    $${PWD}/OAILandlordAccountingModel.h \
    $${PWD}/OAILandlordChaseNoteModel.h \
    $${PWD}/OAILandlordCrmEntry.h \
    $${PWD}/OAILandlordDetailsModel.h \
    $${PWD}/OAILandlordLettingsInspectionModel.h \
    $${PWD}/OAILandlordMaintenanceCertificateModel.h \
    $${PWD}/OAILandlordMaintenanceJobModel.h \
    $${PWD}/OAILandlordMaintenanceJobNoteModel.h \
    $${PWD}/OAILandlordMaintenanceModel.h \
    $${PWD}/OAILandlordMaintenancePreferenceModel.h \
    $${PWD}/OAILandlordPhotoModel.h \
    $${PWD}/OAILandlordPhotoModelResults.h \
    $${PWD}/OAILandlordProfitLossModel.h \
    $${PWD}/OAILandlordProfitLossRowModel.h \
    $${PWD}/OAILandlordProfitLossSectionModel.h \
    $${PWD}/OAILandlordRentArrearsModel.h \
    $${PWD}/OAILandlordRentOustandingItem.h \
    $${PWD}/OAILandlordSettingsModel.h \
    $${PWD}/OAILandlordSummaryModel.h \
    $${PWD}/OAILandlordSummaryTenancyModel.h \
    $${PWD}/OAILandlordTenancyModel.h \
    $${PWD}/OAILettingsLandlordDocument.h \
# APIs
    $${PWD}/OAIBranchControllerApi.h \
    $${PWD}/OAILandlordControllerApi.h \
    $${PWD}/OAIPhotoControllerApi.h \
    $${PWD}/OAIPropertyControllerApi.h \
    $${PWD}/OAISessionControllerApi.h \
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
    $${PWD}/OAIBranchModel.cpp \
    $${PWD}/OAIBranchModelResults.cpp \
    $${PWD}/OAIKeyValuePair_String_String_.cpp \
    $${PWD}/OAILandlordAccountingEntryModel.cpp \
    $${PWD}/OAILandlordAccountingInvoiceModel.cpp \
    $${PWD}/OAILandlordAccountingModel.cpp \
    $${PWD}/OAILandlordChaseNoteModel.cpp \
    $${PWD}/OAILandlordCrmEntry.cpp \
    $${PWD}/OAILandlordDetailsModel.cpp \
    $${PWD}/OAILandlordLettingsInspectionModel.cpp \
    $${PWD}/OAILandlordMaintenanceCertificateModel.cpp \
    $${PWD}/OAILandlordMaintenanceJobModel.cpp \
    $${PWD}/OAILandlordMaintenanceJobNoteModel.cpp \
    $${PWD}/OAILandlordMaintenanceModel.cpp \
    $${PWD}/OAILandlordMaintenancePreferenceModel.cpp \
    $${PWD}/OAILandlordPhotoModel.cpp \
    $${PWD}/OAILandlordPhotoModelResults.cpp \
    $${PWD}/OAILandlordProfitLossModel.cpp \
    $${PWD}/OAILandlordProfitLossRowModel.cpp \
    $${PWD}/OAILandlordProfitLossSectionModel.cpp \
    $${PWD}/OAILandlordRentArrearsModel.cpp \
    $${PWD}/OAILandlordRentOustandingItem.cpp \
    $${PWD}/OAILandlordSettingsModel.cpp \
    $${PWD}/OAILandlordSummaryModel.cpp \
    $${PWD}/OAILandlordSummaryTenancyModel.cpp \
    $${PWD}/OAILandlordTenancyModel.cpp \
    $${PWD}/OAILettingsLandlordDocument.cpp \
# APIs
    $${PWD}/OAIBranchControllerApi.cpp \
    $${PWD}/OAILandlordControllerApi.cpp \
    $${PWD}/OAIPhotoControllerApi.cpp \
    $${PWD}/OAIPropertyControllerApi.cpp \
    $${PWD}/OAISessionControllerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
