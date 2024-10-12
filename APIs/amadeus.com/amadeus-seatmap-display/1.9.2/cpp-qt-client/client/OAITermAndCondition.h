/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAITermAndCondition.h
 *
 * 
 */

#ifndef OAITermAndCondition_H
#define OAITermAndCondition_H

#include <QJsonObject>

#include "OAIDescription.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIDescription;

class OAITermAndCondition : public OAIObject {
public:
    OAITermAndCondition();
    OAITermAndCondition(QString json);
    ~OAITermAndCondition() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCategory() const;
    void setCategory(const QString &category);
    bool is_category_Set() const;
    bool is_category_Valid() const;

    QString getCircumstances() const;
    void setCircumstances(const QString &circumstances);
    bool is_circumstances_Set() const;
    bool is_circumstances_Valid() const;

    QList<OAIDescription> getDescriptions() const;
    void setDescriptions(const QList<OAIDescription> &descriptions);
    bool is_descriptions_Set() const;
    bool is_descriptions_Valid() const;

    QString getMaxPenaltyAmount() const;
    void setMaxPenaltyAmount(const QString &max_penalty_amount);
    bool is_max_penalty_amount_Set() const;
    bool is_max_penalty_amount_Valid() const;

    bool isNotApplicable() const;
    void setNotApplicable(const bool &not_applicable);
    bool is_not_applicable_Set() const;
    bool is_not_applicable_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_category;
    bool m_category_isSet;
    bool m_category_isValid;

    QString m_circumstances;
    bool m_circumstances_isSet;
    bool m_circumstances_isValid;

    QList<OAIDescription> m_descriptions;
    bool m_descriptions_isSet;
    bool m_descriptions_isValid;

    QString m_max_penalty_amount;
    bool m_max_penalty_amount_isSet;
    bool m_max_penalty_amount_isValid;

    bool m_not_applicable;
    bool m_not_applicable_isSet;
    bool m_not_applicable_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAITermAndCondition)

#endif // OAITermAndCondition_H
