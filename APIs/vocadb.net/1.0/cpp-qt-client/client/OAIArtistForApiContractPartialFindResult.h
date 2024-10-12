/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIArtistForApiContractPartialFindResult.h
 *
 * 
 */

#ifndef OAIArtistForApiContractPartialFindResult_H
#define OAIArtistForApiContractPartialFindResult_H

#include <QJsonObject>

#include "OAIArtistForApiContract.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIArtistForApiContract;

class OAIArtistForApiContractPartialFindResult : public OAIObject {
public:
    OAIArtistForApiContractPartialFindResult();
    OAIArtistForApiContractPartialFindResult(QString json);
    ~OAIArtistForApiContractPartialFindResult() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIArtistForApiContract> getItems() const;
    void setItems(const QList<OAIArtistForApiContract> &items);
    bool is_items_Set() const;
    bool is_items_Valid() const;

    QString getTerm() const;
    void setTerm(const QString &term);
    bool is_term_Set() const;
    bool is_term_Valid() const;

    qint32 getTotalCount() const;
    void setTotalCount(const qint32 &total_count);
    bool is_total_count_Set() const;
    bool is_total_count_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIArtistForApiContract> m_items;
    bool m_items_isSet;
    bool m_items_isValid;

    QString m_term;
    bool m_term_isSet;
    bool m_term_isValid;

    qint32 m_total_count;
    bool m_total_count_isSet;
    bool m_total_count_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArtistForApiContractPartialFindResult)

#endif // OAIArtistForApiContractPartialFindResult_H
