preds = model.predict_proba(X_test)
print(preds)

preds_df = pd.DataFrame(preds[:,1], columns = ['Default Probability'])
preds_df['Defaulter'] = preds_df['Default Probability'].apply(lambda x: 1 if x > 0.34 else 0)
