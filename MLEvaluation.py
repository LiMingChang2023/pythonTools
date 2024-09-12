from sklearn.metrics import confusion_matrix, classification_report
import numpy as np

def evaluation_performance(model, x, y_true, n_cls, onehot=True):
    if onehot:
        train_preds = np.argmax(model.predict(x), axis=1)
        y_true = np.argmax(y_true, axis=1)
    else:
        train_preds = np.round(model.predict(x))
    print(np.unique(train_preds, return_counts=True))
    print(np.unique(y_true, return_counts=True))
    cm = confusion_matrix(y_true, train_preds, labels=[n for n in range(n_cls)])
    report = classification_report(y_true, train_preds, output_dict=True)

    return cm, report