import { useState, useEffect, useCallback } from 'react';
import { PromptItem, FilterState } from '../types';

// Mock data for initial load
const initialPrompts: PromptItem[] = [
  {
    id: '1',
    title: '创意写作助手',
    description: '帮助生成故事创意和情节发展',
    content: '我需要一个科幻故事的创意。故事背景设定在2077年的火星殖民地，主角是一名年轻的工程师。请给我三个独特的故事灵感，每个灵感包含：核心冲突、主要角色和一个意想不到的转折。',
    tags: ['写作', '创意', '科幻'],
    isFavorite: true,
    createdAt: '2024-01-15T10:30:00Z',
    updatedAt: '2024-01-15T10:30:00Z',
  },
  {
    id: '2',
    title: '代码优化建议',
    description: '分析并优化现有代码',
    content: '请分析以下 JavaScript 代码并提供优化建议：\n\nfunction fetchData() {\n  const result = fetch(\'api/data\');\n  return result.then(res => res.json());\n}\n\n请指出潜在问题并提供改进版本。',
    tags: ['编程', 'JavaScript', '优化'],
    isFavorite: false,
    createdAt: '2024-01-16T14:20:00Z',
    updatedAt: '2024-01-17T09:45:00Z',
  },
  {
    id: '3',
    title: '营销文案生成器',
    description: '生成吸引人的营销文案',
    content: '我正在为一款新型智能手表写产品描述。目标受众是25-35岁的科技爱好者。请帮我创作一段吸引人的产品文案，突出其健康监测功能和时尚设计。字数控制在150字左右。',
    tags: ['营销', '文案', '产品'],
    isFavorite: true,
    createdAt: '2024-01-18T08:00:00Z',
    updatedAt: '2024-01-18T08:00:00Z',
  },
  {
    id: '4',
    title: 'SQL 查询优化',
    description: '优化数据库查询性能',
    content: '请帮我优化这个 SQL 查询：\n\nSELECT * FROM orders \nWHERE customer_id = 123 \nAND order_date >= \'2024-01-01\'\nORDER BY total_amount DESC;\n\n数据库中有100万条订单记录。请解释潜在性能问题并提供优化方案。',
    tags: ['编程', 'SQL', '数据库'],
    isFavorite: false,
    createdAt: '2024-01-19T16:30:00Z',
    updatedAt: '2024-01-19T16:30:00Z',
  },
  {
    id: '5',
    title: '旅行攻略策划',
    description: '生成旅行建议和行程规划',
    content: '我计划下个月去日本东京旅游5天。预算中等，喜欢美食和文化体验。请帮我规划一个详细的行程，包括：每天的主要景点、推荐餐厅和交通建议。',
    tags: ['旅行', '攻略', '日本'],
    isFavorite: true,
    createdAt: '2024-01-20T11:00:00Z',
    updatedAt: '2024-01-20T11:00:00Z',
  },
];

const STORAGE_KEY = 'promptvault_data';

export function usePromptManager() {
  const [prompts, setPrompts] = useState<PromptItem[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [filter, setFilter] = useState<FilterState>({
    searchTerm: '',
    selectedTag: null,
    showFavoritesOnly: false,
  });

  // Load data from localStorage on mount
  useEffect(() => {
    const storedData = localStorage.getItem(STORAGE_KEY);
    if (storedData) {
      try {
        setPrompts(JSON.parse(storedData));
      } catch {
        setPrompts(initialPrompts);
      }
    } else {
      setPrompts(initialPrompts);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(initialPrompts));
    }
    setIsLoading(false);
  }, []);

  // Save to localStorage whenever prompts change
  useEffect(() => {
    if (!isLoading && prompts.length > 0) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(prompts));
    }
  }, [prompts, isLoading]);

  // Get all unique tags
  const getTags = useCallback(() => {
    const tagCount: Record<string, number> = {};
    prompts.forEach(prompt => {
      prompt.tags.forEach(tag => {
        tagCount[tag] = (tagCount[tag] || 0) + 1;
      });
    });
    return Object.entries(tagCount).map(([name, count]) => ({ name, count }));
  }, [prompts]);

  // Filter prompts based on current filters
  const filteredPrompts = useCallback(() => {
    return prompts.filter(prompt => {
      // Filter by search term
      if (filter.searchTerm) {
        const searchLower = filter.searchTerm.toLowerCase();
        const matchesSearch =
          prompt.title.toLowerCase().includes(searchLower) ||
          prompt.description.toLowerCase().includes(searchLower) ||
          prompt.content.toLowerCase().includes(searchLower);
        if (!matchesSearch) return false;
      }

      // Filter by selected tag
      if (filter.selectedTag) {
        if (!prompt.tags.includes(filter.selectedTag)) return false;
      }

      // Filter by favorites
      if (filter.showFavoritesOnly) {
        if (!prompt.isFavorite) return false;
      }

      return true;
    }).sort((a, b) => {
      // Favorites first, then by update time
      if (a.isFavorite && !b.isFavorite) return -1;
      if (!a.isFavorite && b.isFavorite) return 1;
      return new Date(b.updatedAt).getTime() - new Date(a.updatedAt).getTime();
    });
  }, [prompts, filter]);

  // Add new prompt
  const addPrompt = useCallback((prompt: Omit<PromptItem, 'id' | 'createdAt' | 'updatedAt'>) => {
    const now = new Date().toISOString();
    const newPrompt: PromptItem = {
      ...prompt,
      id: Date.now().toString(),
      createdAt: now,
      updatedAt: now,
    };
    setPrompts(prev => [...prev, newPrompt]);
    return newPrompt;
  }, []);

  // Update prompt
  const updatePrompt = useCallback((id: string, updates: Partial<PromptItem>) => {
    setPrompts(prev =>
      prev.map(prompt =>
        prompt.id === id
          ? { ...prompt, ...updates, updatedAt: new Date().toISOString() }
          : prompt
      )
    );
  }, []);

  // Delete prompt
  const deletePrompt = useCallback((id: string) => {
    setPrompts(prev => prev.filter(prompt => prompt.id !== id));
  }, []);

  // Toggle favorite
  const toggleFavorite = useCallback((id: string) => {
    setPrompts(prev =>
      prev.map(prompt =>
        prompt.id === id
          ? { ...prompt, isFavorite: !prompt.isFavorite, updatedAt: new Date().toISOString() }
          : prompt
      )
    );
  }, []);

  // Export data
  const exportData = useCallback(() => {
    const dataStr = JSON.stringify(prompts, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `promptvault_backup_${new Date().toISOString().split('T')[0]}.json`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }, [prompts]);

  // Import data
  const importData = useCallback((file: File) => {
    return new Promise<boolean>((resolve) => {
      const reader = new FileReader();
      reader.onload = (e) => {
        try {
          const importedData = JSON.parse(e.target?.result as string);
          if (Array.isArray(importedData)) {
            setPrompts(importedData);
            resolve(true);
          } else {
            resolve(false);
          }
        } catch {
          resolve(false);
        }
      };
      reader.readAsText(file);
    });
  }, []);

  // Update filter
  const updateFilter = useCallback((updates: Partial<FilterState>) => {
    setFilter(prev => ({ ...prev, ...updates }));
  }, []);

  // Reset filters
  const resetFilters = useCallback(() => {
    setFilter({
      searchTerm: '',
      selectedTag: null,
      showFavoritesOnly: false,
    });
  }, []);

  return {
    prompts,
    filteredPrompts,
    isLoading,
    filter,
    tags: getTags(),
    addPrompt,
    updatePrompt,
    deletePrompt,
    toggleFavorite,
    exportData,
    importData,
    updateFilter,
    resetFilters,
    totalCount: prompts.length,
  };
}
