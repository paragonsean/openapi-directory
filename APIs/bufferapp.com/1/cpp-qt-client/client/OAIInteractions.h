/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIInteractions.h
 *
 * 
 */

#ifndef OAIInteractions_H
#define OAIInteractions_H

#include <QJsonObject>

#include "OAIInteractions_interactions_inner.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIInteractions_interactions_inner;

class OAIInteractions : public OAIObject {
public:
    OAIInteractions();
    OAIInteractions(QString json);
    ~OAIInteractions() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIInteractions_interactions_inner> getInteractions() const;
    void setInteractions(const QList<OAIInteractions_interactions_inner> &interactions);
    bool is_interactions_Set() const;
    bool is_interactions_Valid() const;

    double getTotal() const;
    void setTotal(const double &total);
    bool is_total_Set() const;
    bool is_total_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIInteractions_interactions_inner> m_interactions;
    bool m_interactions_isSet;
    bool m_interactions_isValid;

    double m_total;
    bool m_total_isSet;
    bool m_total_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIInteractions)

#endif // OAIInteractions_H
