import { useChatContext } from '../context/ChatContext';

const UserInput = () => {
  const { inputValue, setInputValue, sendMessage, loading } = useChatContext();

  return (
    <form onSubmit={sendMessage} className="p-4 flex gap-2 border-t">
      <input
        value={inputValue}
        onChange={e => setInputValue(e.target.value)}
        className="flex-1 border p-2 rounded"
        placeholder="Type your message..."
      />
      <button
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        {loading ? '...' : 'Send'}
      </button>
    </form>
  );
};

export default UserInput;
