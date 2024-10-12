/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIFrequentFlyerInfo.h
 *
 * 
 */

#ifndef OAIFrequentFlyerInfo_H
#define OAIFrequentFlyerInfo_H

#include <QJsonObject>

#include "OAILocalizedString.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAILocalizedString;

class OAIFrequentFlyerInfo : public OAIObject {
public:
    OAIFrequentFlyerInfo();
    OAIFrequentFlyerInfo(QString json);
    ~OAIFrequentFlyerInfo() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getFrequentFlyerNumber() const;
    void setFrequentFlyerNumber(const QString &frequent_flyer_number);
    bool is_frequent_flyer_number_Set() const;
    bool is_frequent_flyer_number_Valid() const;

    OAILocalizedString getFrequentFlyerProgramName() const;
    void setFrequentFlyerProgramName(const OAILocalizedString &frequent_flyer_program_name);
    bool is_frequent_flyer_program_name_Set() const;
    bool is_frequent_flyer_program_name_Valid() const;

    QString getKind() const;
    void setKind(const QString &kind);
    bool is_kind_Set() const;
    bool is_kind_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_frequent_flyer_number;
    bool m_frequent_flyer_number_isSet;
    bool m_frequent_flyer_number_isValid;

    OAILocalizedString m_frequent_flyer_program_name;
    bool m_frequent_flyer_program_name_isSet;
    bool m_frequent_flyer_program_name_isValid;

    QString m_kind;
    bool m_kind_isSet;
    bool m_kind_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFrequentFlyerInfo)

#endif // OAIFrequentFlyerInfo_H
